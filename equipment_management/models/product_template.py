from odoo import api, fields, models, _


class product_template(models.Model):
    _inherit = 'product.template'

    pass_duration = fields.Char('Pass Duration')
    employee_name = fields.Char('Employee Name')
    contact = fields.Char('Contact')



