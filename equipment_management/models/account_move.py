from odoo import api, fields, models, _

class account_move(models.Model):
    _inherit = 'account.move'

    age = fields.Char('Age')
    po_no = fields.Char('Po No')