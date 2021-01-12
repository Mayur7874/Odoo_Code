from odoo import models , fields ,api ,_


class vacancy_info_spt(models.Model):
    _name = 'vacancy.info.spt'
    _description = "vacancy info spt"


    name = fields.Selection([('cash','Cashier'),('management','Management'),('sales','Sales'),('groundstaff','GroundStaff')], string='Vacancy Department')
    total_vac = fields.Integer('Toatal Vacancy')
    vac_bra_name = fields.Many2one('branch.info.spt', 'Brach name ')
    vac_shift= fields.Selection([('morning','Morning'),('evening','Evening')], string='Time')
    active = fields.Boolean('Active')

