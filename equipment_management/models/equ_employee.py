from odoo import fields, models ,api,_ 

class equ_employee(models.Model):
    _name = "equ.employee"
    _description = "equ employee"



    name = fields.Char("Employee Name")
    contact = fields.Char("Contact")
    post = fields.Char('Employee Post')
    address = fields.Char("Employee Address")
    email = fields.Char("Employee Email")
