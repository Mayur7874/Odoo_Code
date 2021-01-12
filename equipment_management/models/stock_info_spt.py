from odoo import api, fields, models,_


class stock_info_spt(models.Model):
    _inherit = 'stock.info.spt'

    employee_name = fields.Char("Employee Name")
