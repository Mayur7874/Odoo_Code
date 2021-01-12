from odoo import models , fields ,api ,_

class display_interface(models.Model):
    _name = "display.interface"
    _description = "display interface"

    user_tokan_numbe = fields.Char('Tokan Number')
    counter_number = fields.Integer('Counter  Number')
    employee = fields.Char('Employee Name')
    user = fields.Char('User Name')
    user_display_status = fields.Selection([('active','Active'),('dective','Deactive')],string='Disply Status')
     
    
    