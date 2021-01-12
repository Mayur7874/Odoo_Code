from odoo import models , fields ,api ,_

class que_product(models.Model):
    _name = "que.product"
    _description = "que product"
    _rec_name = "model"



    category = fields.Selection([('tv','TV'),('phone','Phone'),('laptop','Laptop')], string='Product Category')
    model = fields.Char('Product Model ') 
    dec = fields.Char('Product Description')
    pro_warrenty = fields.Char('Warrenty Time')
    pro_releases_date = fields.Date('Releases Date')
    prices = fields.Float('Product Prices')