from odoo import models , fields ,api ,_


class example_product(models.Model):
    _name = "example.product"
    _description = 'example product'

    name = fields.Char('Product Name')
    price = fields.Float('Product Amount')
    stock =  fields.Integer(string='Stock')
    
