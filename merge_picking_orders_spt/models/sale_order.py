
from odoo import models, fields, api, _


class sale_order(models.Model):
    _inherit = 'sale.order'

    
    sale_order_ref_ids = fields.Many2many('sale.order','sale_order_picking_order_id','sale_id','picking_id','Sale Order')
    merge_sale_order =  fields.Boolean('Merge Sale Order')


    def prepare_order_line(self, line):
        vals = {
            'product_id': line.product_id.id,
            'name': line.name,
            'product_uom_qty': line.product_uom_qty,
            'qty_delivered': line.qty_delivered,
            'qty_invoiced': line.qty_invoiced,
            'customer_lead': line.customer_lead,
            'price_unit': line.price_unit,
            'tax_id': line.tax_id.ids,
            'price_subtotal': line.price_subtotal,
        }
        return vals


    def acton_merge_sale_orders(self, order_ids):
        partner_id = order_ids[0].partner_id
        payment_terms = order_ids[0].payment_term_id
        merged_order_ids=[]
        new_sale_order = self.env['sale.order'].create(
            {'partner_id': partner_id.id})
        new_sale_order.payment_term_id = payment_terms.id
        for order_id in order_ids:
            merged_order_ids.append(order_id.id)
            for line in order_id.order_line:
                vals = self.prepare_order_line(line)
                vals['order_id'] = new_sale_order.id
                new_sale_order_line = self.env['sale.order.line'].create(vals)
            order_id.action_cancel()
        new_sale_order.sale_order_ref_ids = [(6,0,merged_order_ids)]
        new_sale_order.merge_sale_order = True
        new_sale_order.action_confirm()
        
    def action_marge_sale_order_list(self):

        return {
            'name': _('sale order'),
            'domain': [('id', 'in', self.sale_order_ref_ids.ids)],
            'res_model': 'sale.order',
            'view_mode': 'tree',
            'type': 'ir.actions.act_window',
        }