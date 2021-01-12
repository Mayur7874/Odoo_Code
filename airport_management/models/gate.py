from odoo import models, fields, api, _


class gate(models.Model):
    _name = "gate"
    _description = 'gate'

    name = fields.Char('Gate Number') 
    category = fields.Selection([('national','National'),('international','International')], string='Gate Category')