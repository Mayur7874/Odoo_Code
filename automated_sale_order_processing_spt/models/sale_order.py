from odoo import models, fields, api, _
# from pprint import pformat
from datetime import timedelta


class sale_order(models.Model):
    _inherit = 'sale.order'

    workflow_process_id = fields.Many2one(
        'auto.sale.workflow.spt', 'Workflow Process', store=True, related="partner_id.workflow_process_id")
    auto_process_state = fields.Selection(
        [('processed', 'Processed'), ('error_state', 'Error')])

    # sale order policy

    confirm_order = fields.Boolean('Confirm Order',store=True)
    validation_picking = fields.Boolean('Validation Picking', store=True)
    create_invoice = fields.Boolean('Create Invoice')
    confirm_invoice = fields.Boolean('Confirm Invoice')
    register_payment = fields.Boolean('Register Payment')
    force_inventory_available = fields.Boolean('Force Inventory Available')
    expected_days = fields.Integer(string='Expected Days')
    shipping_policy_spt = fields.Selection([('direct', 'As soon as possible'), (
        'one', 'When all products are ready')], string="Shipping Policy")
    invoice_policy_spt = fields.Selection(
        [('order', 'Ordered quantities'), ('delivery', 'Delivered quantities')], string="Invoice Policy")
    payment_journal_id = fields.Many2one(
        'account.journal', string='Payment Journal', domain="[('type', 'in', ['bank', 'cash'])]")
    error_note = fields.Text('Message')
    auto_process_error_state = fields.Selection([('order', 'Sale Order'), ('delivery', 'Delivery'), (
        'invoice', 'Invoice')], string='Error State', help='Some Error In Your Order,So Please Check Your Sale Order In Auto Process Tab')
    is_eligible = fields.Boolean('Eligible Autoprocess')

    @api.onchange('workflow_process_id')
    def auto_process(self):
        for sale_order in self:
            if sale_order.workflow_process_id:
                sale_order.is_eligible = True
                sale_order.confirm_order = sale_order.workflow_process_id.confirm_order
                sale_order.validation_picking = sale_order.workflow_process_id.validation_picking
                sale_order.create_invoice = sale_order.workflow_process_id.create_invoice
                sale_order.confirm_invoice = sale_order.workflow_process_id.confirm_invoice
                sale_order.register_payment = sale_order.workflow_process_id.register_payment
                sale_order.force_inventory_available = sale_order.workflow_process_id.force_inventory_available
                sale_order.expected_days = sale_order.workflow_process_id.expected_days
                sale_order.shipping_policy_spt = sale_order.workflow_process_id.shipping_policy_spt
                sale_order.invoice_policy_spt = sale_order.workflow_process_id.invoice_policy_spt
                sale_order.payment_journal_id = sale_order.workflow_process_id.payment_journal_id
            else:
                sale_order.is_eligible = False
                sale_order.confirm_order = False
                sale_order.validation_picking = False
                sale_order.create_invoice = False
                sale_order.confirm_invoice = False
                sale_order.register_payment = False
                sale_order.force_inventory_available = False
                sale_order.expected_days = False
                sale_order.shipping_policy_spt = False
                sale_order.invoice_policy_spt = False
                sale_order.payment_journal_id = False
    
    @api.onchange('shipping_policy_spt')
    def set_commitment_date (self):
        for sale_order in self:
            if sale_order.shipping_policy_spt in ['one']:
                sale_order.picking_policy, sale_order.commitment_date = sale_order.shipping_policy_spt, sale_order.date_order + timedelta(sale_order.expected_days)
            else:
                sale_order.picking_policy = 'direct'
                sale_order.commitment_date = False
    

    def action_auto_process_spt(self):
        auto_process_eligible = self.filtered(lambda sale_order: sale_order.is_eligible == True and sale_order.state not in ['cancel','done'])
        error_sale_order = []
        for sale_order in auto_process_eligible:
            auto_process_error_note = ''
            if sale_order.auto_process_error_state:
                sale_order.auto_process_error_state = False
                
            # confirm order
            if sale_order.confirm_order and sale_order.state in ['draft','sent']:
                sale_order.action_confirm()

            #  check availability & validate picking
            if sale_order.picking_ids and sale_order.validation_picking:
                auto_process_picking_ids = sale_order.picking_ids.filtered(lambda picking_ids: picking_ids.state in ['confirmed','assigned'])
                for picking_id in auto_process_picking_ids:
                    picking_id.action_assign() 
                    picking_lines = picking_id.move_ids_without_package
                        
                    if sale_order.force_inventory_available:
                        for picking_line in picking_lines:
                            picking_line.quantity_done = picking_line.product_uom_qty
                        picking_id.button_validate()

                    else:
                        zero_qty_product = []
                        not_availabel_product = []
                        for picking_line in picking_lines:
                            picking_line.quantity_done = picking_line.forecast_availability
                            if picking_line.forecast_availability == 0:
                                zero_qty_product.append(picking_line)
                            if picking_line.product_uom_qty != picking_line.forecast_availability:
                                not_availabel_product.append(picking_line)

                        if not zero_qty_product:
                            if not_availabel_product:
                                validate = picking_id.button_validate()
                                ctx = validate['context']
                                back_order = self.env['stock.backorder.confirmation'].with_context(ctx).create({'pick_ids': [(4, picking_id.id)]})
                                back_order_tranfer = self.env['stock.backorder.confirmation.line'].create({'to_backorder': True, 'picking_id': picking_id.id, 'backorder_confirmation_id': back_order.id})
                                back_order.process()
                            else:
                                picking_id.button_validate()

                        if zero_qty_product and sale_order.invoice_policy_spt in ['delivery']:
                            sale_order.auto_process_error_state = 'delivery'
                            auto_process_error_note = 'You cannot Picking  transfer if no quantities and reserved quantities is not done With Delivered quantities Invoice Policy'

            # create invoice & create invoice_line_value
            if sale_order.create_invoice:
                invoive_policy_list = []
                # order_line filter service_products and consu_and_storable product
                service_products_order_line = sale_order.order_line.filtered(lambda order_line: order_line.product_id.type == 'service' and order_line.invoice_status in ['no','to invoice'])
                service_products_order_quantities = sale_order.order_line.filtered(lambda order_line: order_line.product_id.type == 'service' and order_line.product_id.invoice_policy in ['order'] and order_line.invoice_status in ['no','to invoice'])
                # consu and product
                consu_and_storable_order_line = sale_order.order_line.filtered(lambda order_line: order_line.product_id.type in ['consu','product'] and order_line.invoice_status in ['no','to invoice'])
               
                if sale_order.invoice_policy_spt in ['delivery']:
                    for order_line in consu_and_storable_order_line:
                        if order_line.qty_invoiced == 0.0:
                            order_line.qty_to_invoice = order_line.qty_delivered
                        if order_line.qty_delivered == 0:
                            invoive_policy_list.append(order_line)

                if sale_order.invoice_policy_spt in ['order']:
                    for order_line in consu_and_storable_order_line:
                        if order_line.qty_invoiced == 0.0:
                            order_line.qty_to_invoice = order_line.product_uom_qty

                if service_products_order_line:
                    for order_line in service_products_order_line:
                        if order_line.product_id.invoice_policy in ['order']:
                            order_line.qty_to_invoice = order_line.product_uom_qty
                        else: 
                            if not service_products_order_quantities and not consu_and_storable_order_line:
                                invoive_policy_list.append(order_line)


                if not invoive_policy_list and not sale_order.auto_process_error_state:
                    if sale_order.invoice_status in ['no','to invoice'] or sale_order.invoice_id.state == 'cancel':
                        order_id = {
                            'active_ids': sale_order.ids,
                            'active_model': 'sale.order',
                        }
                        if len(sale_order) == 1:
                            order_id.update({'active_id': sale_order.id})

                        sale_advance_payment_inv_obj = self.with_context(order_id).env['sale.advance.payment.inv']

                        ctx = {
                            'advance_payment_method': 'delivered',
                            'currency_id': sale_order.currency_id.id, }

                        sale_advance_payment_inv_id = sale_advance_payment_inv_obj.create(ctx)
                        sale_advance_payment_inv_id.create_invoices()

                if invoive_policy_list and not sale_order.auto_process_error_state:
                    sale_order.auto_process_error_state = 'invoice'
                    auto_process_error_note = 'Your Invoice policy Is Delivered Quantities And  WithOut Validate Picking You Can Not Creating Invoice , If Your Select Product In Product Type Is Service,Before Auto Process You Change Invoice Policy and Service Product Is Not Validate For Delivered Quantities Invoice policy'

        #             # confirm invoice
            if sale_order.confirm_invoice:
                auto_process_invoice = sale_order.invoice_ids.filtered(lambda invoice_ids: invoice_ids.state in ['draft'])
                for invoice_id in auto_process_invoice:
                    invoice_id.action_post()
                # registe_payment
            if sale_order.register_payment:
                auto_process_register_payment = sale_order.invoice_ids.filtered(lambda invoice_ids: invoice_ids.payment_state in ['not_paid','partial'] and invoice_ids.state not in 'cancel')
                for invoice_id  in auto_process_register_payment:
                    invoice_active_id = {'active_model': 'account.move',
                                            'active_ids': invoice_id.id,}
                    register_payment_ctx = {'journal_id': sale_order.payment_journal_id.id,
                                            'amount': invoice_id.amount_residual,
                                            'payment_date': invoice_id.invoice_date,
                                            'communication': invoice_id.name, }
                    register_payment = self.with_context(invoice_active_id).env['account.payment.register'].create(register_payment_ctx)
                    register_payment.action_create_payments()

            if sale_order.auto_process_error_state:
                sale_order.auto_process_state = 'error_state'
                sale_order.error_note = auto_process_error_note
                error_sale_order.append(sale_order.id)
                self.env.cr.commit()
            else:
                sale_order.auto_process_state = 'processed'
                if sale_order.error_note:
                    sale_order.error_note = False
                

        if len(self) > 1 and error_sale_order:
            return {
                'name': _('Erro Sale Order'),
                'domain': [('id', '=', error_sale_order)],
                'res_model': 'sale.order',
                'view_mode': 'tree',
                'views': [(self.env.ref('sale.view_quotation_tree_with_onboarding').id, 'tree'), (False, 'form')],
                'type': 'ir.actions.act_window',
            }

    def action_error_meassage(self):
        pass
