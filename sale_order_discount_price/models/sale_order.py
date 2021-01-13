from odoo import models, fields, api, _


class sale_order(models.Model):
    _inherit = 'sale.order'

    discount_type = fields.Selection(
        [('percentage', 'Percentage'),('manual', 'Manual')], string='Discount Type')
    total_discount = fields.Float("Toatl Discount")
     
    @api.depends('order_line.price_total','total_discount','discount_type')
    def _amount_all(self):
        super(sale_order,self)._amount_all()
        if self.discount_type == 'percentage':
            self.amount_total =  self.amount_untaxed - (self.amount_untaxed * self.total_discount) / 100 
            self.amount_total += self.amount_tax
        if self.discount_type == 'manual':
            self.amount_total = self.amount_untaxed - self.total_discount
            self.amount_total += self.amount_tax

