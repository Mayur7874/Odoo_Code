from odoo import models , fields ,api ,_

class employee_info(models.Model):
    _name = "employee.info"
    _description = 'company mangement model'

    name = fields.Char('Name')
    address = fields.Char('Address')
    mo_number = fields.Char('mo_number ')
    dob_date = fields.Date('Dob_date')
    add_file = fields.Binary('Document file')
    post = fields.Char('Post')
    select_Resident = fields.Selection([('abc','India'),('xyz','NRI')], string='Nationality')





