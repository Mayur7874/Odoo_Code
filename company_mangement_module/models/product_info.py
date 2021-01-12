from odoo import models , fields ,api ,_

class product_info(models.Model):
    _name = 'product.info'
    _description = 'Product info'


    Product_info = fields.Selection([('abc','Web'),('xyz','Ios'),('111','Erp')], string='ProductName1234')
    E_Name = fields.Char('EmployeeName')
