from  odoo import fields , models,api ,_ 

class equ_request(models.Model):
    _name = "equ.request"
    _description = "equ request"

    request_employee_name = fields.Many2one('equ.employee','employee Name')
    equipment_name = fields.Char('Equipment Name')
    reason = fields.Char('Reason')
    post = fields.Char('Post')
    selection = fields.Selection([('approval','Approval'),('disapproval','Disapproval')], string='Request')
   


    @api.onchange('request_employee_name')
    def onchange_post_employee_name(self):
        for rec in self:
            if rec.request_employee_name:
                rec.post = rec.request_employee_name.post
