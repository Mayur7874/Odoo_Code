from odoo import models , fields ,api ,_
from datetime import date
 
class que_tokan_interface(models.Model):
    _name = "que.tokan.interface"
    _description = 'que tokan interface'


    number = fields.Char("Tokan Number",default = lambda self : self.env['ir.sequence'].next_by_code('token_ref'))
    date = fields.Date('Tokan Date',default= date.today())
    username = fields.Char('Customar Name')
    usercontact = fields.Char('Contact')
    tokan_model_rel = fields.Many2many('que.product','tokan_model_rel','tokan_id','model_id','Model')
    tokan_Problam_rel = fields.Many2many('que.problam','tokan_problam_rel','tokan_id','problam_id','Probalm Selection')
    counternumber = fields.Integer('Employee Counter')
    employeename = fields.Char('Employee Name')
    status = fields.Selection([('hold','HOLD'),('done','DONE')],'Tokan Status',default="hold")
 
