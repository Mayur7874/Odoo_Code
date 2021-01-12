from odoo import models , fields ,api ,_

class branch_info_spt(models.Model):
    _name = "branch.info.spt"
    _description = 'branch info spt'
    _rec_name = 'bra_name'


    bra_name = fields.Char('Branch Name')
    bra_contact = fields.Char('Branch Contact Number')
    bra_address = fields.Char('Branch Address')

 
 
    bra_to_emp_ids = fields.One2many('employee.info.spt','emp_to_bra_id','Employess')
    mm_emp_ids = fields.Many2many('employee.info.spt','bra_emp_rel_spt','bra_id','emp_id','Employees Selection')
   



    def action_bra_wise_info(self):
        for rec in self:
            # emp_obj = self.env['employee.info.spt']
            # # employee_name = rec.emp_name
            # employee_names  = []
            # for ids in emp_obj:
            #     employee_names.append(ids.id)
            # return {
            # 'name' : _('branch'),
            # 'domain' : [('id','in',employee_names)],
            # 'view_type' : 'form',
            # 'res_model' : 'employee.info.spt',
            # 'view_id' : False,
            # 'view_mode' : 'tree,form',
            # 'type' : 'ir.actions.act_window',
            # }

            emp_obj = self.env['employee.info.spt']

            b_id = rec.id
            emp = emp_obj.search([('emp_to_bra_id','=',b_id)])
            e_list = []

            for ids in emp:
                e_list.append(ids.id)

            return {
            'name' : _('employee'),
            'domain' : [('id','in',e_list)],
            'res_model' : 'employee.info.spt',
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',
            }    




            

    