from odoo import fields,models,api,_

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    is_product_pack = fields.Boolean('Is Product Pack',related="product_id.is_product_pack")