from odoo import models, fields, api, _


class res_partner(models.Model):
    _inherit = 'res.partner'


    product = fields.One2many('sale.order.line', 'order_partner_id', 'Product')

    sale_product = fields.One2many('purchase.order.line', 'partner_id', 'Sale_product')
    
    



