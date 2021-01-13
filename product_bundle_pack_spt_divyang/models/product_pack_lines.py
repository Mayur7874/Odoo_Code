from odoo import models, fields, api, _


class product_pack_lines(models.Model):
    _name = 'product.pack.lines'

    product_id = fields.Many2one('product.product',string = "Product")
    product_tmpl_id = fields.Many2one('product.template',related="product_id.product_tmpl_id")
    product_qty = fields.Float('Quantity',default=1)
    qty_available = fields.Float(string='Availabel Quantity', store=True,related='product_id.qty_available')
    bundle_template_id = fields.Many2one('product.template','Bundle Origin')
    lst_price = fields.Float('Sale Price',related="product_tmpl_id.lst_price")