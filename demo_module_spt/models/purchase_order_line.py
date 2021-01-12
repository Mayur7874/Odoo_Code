from odoo import models, fields, api, _


class purchase_order_line(models.Model):
    _inherit = 'purchase.order.line'


    image = fields.Binary('Product Image', related='product_id.image_1920')
   
