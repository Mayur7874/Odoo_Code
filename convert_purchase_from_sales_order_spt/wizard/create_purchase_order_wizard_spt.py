from odoo import fields, models, api, _
from datetime import datetime


class create_purchase_order_wizard_spt(models.TransientModel):
    _name = "create.purchase.order.wizard.spt"

    partner_id = fields.Many2one('res.partner', string="Vendor")
    sale_order_date = fields.Datetime(
        string='Order Date', default=datetime.now())
    sale_order_lines_ids = fields.Many2many(
        'sale.order.line', 'sale_order_purches__order_rel', 'sale_order_id', 'purchase_order_id', string='sale order line')

    def creat_purches_order_line(self, line_id):
        vals = {
            'product_id': line_id.product_id.id,
            'name': line_id.name,
            'product_qty': line_id.product_uom_qty,
            'price_unit': line_id.price_unit,
            'taxes_id': [(6,0,line_id.tax_id.ids)],
            'price_subtotal': line_id.price_subtotal,}
        return vals


    def action_create_purchase_order(self):
        purches_order_vals = {'partner_id': self.partner_id.id}
        purches_order_obj = self.env['purchase.order'].create(purches_order_vals)
        line_vals = []
        for line_id in self.sale_order_lines_ids:
            purchase_vals = self.creat_purches_order_line(line_id)
            line_vals.append([0, 0, purchase_vals])
        purches_order_obj['order_line'] = line_vals
    
        
        
