from odoo import api, fields, models, _

class res_config_settings(models.TransientModel):
    _inherit = 'res.config.settings'

    contact = fields.Char('Contact')