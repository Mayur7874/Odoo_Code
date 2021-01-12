from odoo import models, fields, api, _


class route(models.Model):
    _name = "route"
    _description = 'route'

    name = fields.Char('Route') 
    category = fields.Selection([('national','National'),('international','International')], string='Route Category')
