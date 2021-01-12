from odoo import models , fields ,api ,_

class counter_interface(models.Model):
    _name = "counter.interface"
    _description = "counter interface"
    _rec_name = 'uname'


    uname = fields.Char("User Name")
    uemail= fields.Char('Email')
    counter_model_rel = fields.Many2many('que.product','counter_model_rel','counter_id','model_id','Model')
    counter_problam_rel= fields.Many2many('que.problam','counter_problam_rel','counter_id','problam_id','Probalm')
    bill = fields.Char('Bill No')
    warrenty = fields.Selection([('active','Active'),('deactive','Deactive')],string="Warrenty") 
    tokan_number = fields.Char('Tokan Number')  
    t_date = fields.Date('Tokan Date')
    counter_number = fields.Integer('Counter Number')
    device_reparing_date = fields.Date('Reparing Date')
    total_reparing_day =fields.Char('Total Reparing Day')
    user_rating =fields.Char('User Rating')
    device_status = fields.Selection([('hold','HOLD'),('done','DONE')], string='Device Status') 
    display_status = fields.Selection([('active','Active'),('dective','Deactive')],string='Disply Status')
    counter_status = fields.Selection([('active','Active'),('deactive','Deactive'),('busy','Busy'),('free','Free')],'Counter Status',default="active")



    @api.onchange('counter_status')
    def onchange_counter_status(self):
        emp_obj = self.env['que.employee']
        for rec in self:
            emp = emp_obj.search([('counter','=',rec.counter_number)])
            emp.write({'emp_counter_status' : rec.counter_status})

            


