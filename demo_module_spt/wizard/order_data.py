from odoo import fields, models, api, _


class order_data(models.TransientModel):
    _name = "order.data"

    sale = fields.Many2one('sale.order', 'Sale')
    # sale_order_line = fields.Many2many(
    #     'sale.order.line', 'sale_order_rel', 'sale_id', 'order_id', 'Sale Order')
        
    sale_order_line = fields.One2many('sale.order.line', 'order_id')
    
    # fenil_total =  fields.Char('Fenil Total')

    @api.onchange('sale')
    def onchange_field(self):
        sol = self.sale.order_line
        # for each in sol:
        self.sale_order_line = sol

