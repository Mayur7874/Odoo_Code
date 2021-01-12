from odoo import models, fields, api, _


class account_payment(models.Model):
    _inherit = 'account.payment'

    active_selection = fields.Boolean('Show Commission')

    sale_commission_ids = fields.One2many(
        'account.move.line.spt', 'account_payment_id')

