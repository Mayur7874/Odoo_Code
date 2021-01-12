from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError


class sale_order(models.Model):
    _inherit = 'sale.order'

    payment_date = fields.Datetime(string='Payment')

    account_move_id = fields.Many2one('account.move', string='Account Move')

    # commission_ids = fields.One2many('account.move.line.spt', 'sale_order_id')
    commission_ids = fields.Many2many(
        'account.move.line.spt', 'sale_order_id')

    partner_child_ids = fields.Many2many('res.partner', 'partner_child_rel')

    product_id = fields.Many2one('product.template', string='Product')

    def action_order_spt(self):
        self.action_confirm()
        self.picking_ids.button_validate()
        avc = self.env['stock.immediate.transfer'].create(
            {'pick_ids': [(4, self.picking_ids.id)]})
        avc.process()

    def action_order_data(self):
        return {
            'name': _('order data'),
            'view_mode': 'form',
            'res_model': 'order.data',
            'type': 'ir.actions.act_window',
            'context': {'default_sale': self.id, },
            'target': 'new',
        }

    # def action_fenil_data(self):
    #     account_move_obj = self.env['account.move']
    #     for rec in self:
    #         account_move_line = account_move_obj.search([('partner_id','=',49)])
    #         total = 0
    #         for invoice in account_move_line:
    #             total += invoice.amount_total

    #     return {
    #         'name': _('order data'),
    #         'view_mode': 'form',
    #         'res_model': 'order.data',
    #         'type': 'ir.actions.act_window',
    #         'context': {'default_fenil_total': total},
    #         'target': 'new',
    #     }

    @api.onchange('partner_id')
    def set_payment_date(self):
        self.payment_date = False
        if self.payment_term_id:
            payment = self.payment_term_id.line_ids.days
            self.payment_date = self.date_order + timedelta(payment)

    @api.onchange('partner_id')
    def partner_child_ids_onchange_field(self):
        self.partner_child_ids = self.partner_id.child_ids.ids
        return {'domain': {'partner_child_ids': [('id', '=', self.partner_id.child_ids.ids)]}}

    @api.onchange('partner_id')
    def compute_commision_id(self):
        self.ensure_one()
        if self.partner_id.id:
            self.commission_ids.unlink()
            self.set_commision_id(self.partner_id.id,
                                  self.id, self.amount_total)

            if self.partner_id.child_ids:
                # self.partner_child_ids = self.partner_id.child_ids.ids
                for child in self.partner_id.child_ids:
                    self.set_commision_id(child.id, self.id, self.amount_total)
            else:
                self.partner_child_ids = False

    def set_commision_id(self, partner_id, sale_order_id, subtotal):
        self.commission_ids = [
            (0, 0, {'partner_id': partner_id, 'sale_order_id': sale_order_id, 'subtotal': subtotal})]
        return self.commission_ids

    @api.onchange('amount_total')
    def subtotal_onchange(self):
        if self.amount_total:
            self.commission_ids.subtotal = self.amount_total
            for commission_id in self.commission_ids:
                commission_id.fixed_amount = False
                commission_id.percentage_amount = False
                commission_id.total = False
        if self.amount_total == 0.0:
            for commission_id in self.commission_ids:
                commission_id.fixed_amount = False
                commission_id.percentage_amount = False
                commission_id.total = False

    # @api.onchange('partner_id')
    # def sale_order_data_line_ids_onchange_field(self):
    #     if self.partner_id:
    #         if self.partner_id.child_ids:
    #             self.partner_child_ids = self.partner_id.child_ids.ids
    #             self.commission_id.unlink()
    #             for child in self.partner_child_ids:
    #                 values_child_ids = {
    #                     'partner_id': child._origin.id,
    #                     'sale_order_id': self.id
    #                 }
    #                 self.env['account.move.line.spt'].create(
    #                     values_child_ids)
    #         else:
    #             self.partner_child_ids = False
    #             self.commission_id.unlink()
    #             self.commission_id = False
    # def test_report(self):
    #     a=[]
    #     for i in range(0,10):
    #         a.append(i)
    #     return a

    def action_excel_report(self):
        return {
            'name':_('Wizard'),
            'type':'ir.actions.act_window',
            'model':'sales.report.for.sales.person.wizard.spt',
            'view_mode':'form',
            'context':{

            },
            'target':'new',
        }