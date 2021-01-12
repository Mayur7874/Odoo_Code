from odoo import models, fields, api, _


class flight(models.Model):
    _name = "flight"
    _description = 'flight'

    name = fields.Char("Flight Name")
    Aviation_id = fields.Many2one('airline', string="Airline Name")
    country = fields.Char(
        "Country Name", related='Aviation_id.country', store=True)
    flight_route_id = fields.Many2one('route', string='Flight Route')
    category = fields.Selection(
        [('national', 'National'), ('international', 'International')], string='Flight Category')
