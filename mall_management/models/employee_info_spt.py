from odoo import models , fields ,api ,_

class employee_info_spt(models.Model):
    _name = "employee.info.spt"
    _description = 'employee info model'
    _rec_name = 'emp_name'

    emp_name = fields.Char('Employee Name')
    emp_address = fields.Char('Employee Address')
    emp_contact = fields.Char('ContactNumber')
    emp_dob_date = fields.Date('Dob Date')
    emp_joining_date = fields.Date('Joining Date')
    emp_last_date = fields.Date('Last Date')
    emp_doc_file = fields.Binary('Employee Document file')
    emp_shift = fields.Selection([('morning','Morning'),('evening','Evening')], string='Shift Time')
    emp_department = fields.Selection([('cash','Cashier'),('management','Management'),('sales','Sales'),('groundstaff','GroundStaff')], string='Department')
    emp_present = fields.Boolean('Present')
    emp_image = fields.Binary('Image')
    emp_to_bra_id = fields.Many2one('branch.info.spt','Employee Branch')
    emp_all_vac = fields.Many2many('vacancy.info.spt','vac_to_emp_rel_spt','emp_all_id','vac_all_id','Branch  Selection')
    
    # mm_bra_ids = fields.Many2many('branch.info.spt','bra_emp_rel_spt','emp_id','bra_id','Branch Selection')
    

    