from odoo import models , fields ,api ,_

class que_employee(models.Model):
    _name = "que.employee"
    _description = 'que employee'


    name = fields.Char('Name')
    address =fields.Char('Address')
    contact =fields.Char("Contact")
    dob =fields.Date("Dob")
    document =fields.Binary('Document File')
    counter =fields.Integer('Counter Number')
    emp_counter_status = fields.Selection([('active','Active'),('deactive','Deactive'),('busy','Busy'),('free','Free')],'Counter Status',default="active")
    employess_status = fields.Selection([('open','OPEN'),('close','CLOSE')],'Employee Status', default='close')
    

    @api.model
    def create(self,vals):
        pop = super(que_employee,self).create(vals)
        pop.address = 'Surat'
    
        return pop

    def write(self,vals):
        if not self.address == 'Surat' :
            vals['address'] = 'modasa'
        pop = super(que_employee,self).write(vals)

        

              
