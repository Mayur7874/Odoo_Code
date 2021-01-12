from odoo import models, fields, api, _


class sale_order_line(models.Model):
    _inherit = 'sale.order.line'


    image = fields.Binary('Product Image', related='product_id.image_1920')


   
    