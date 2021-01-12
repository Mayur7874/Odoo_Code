from odoo import api, fields, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    contact = fields.Char('Contact')