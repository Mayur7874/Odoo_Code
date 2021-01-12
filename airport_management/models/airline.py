from odoo import models , fields ,api ,_

class airline(models.Model):
    _name = "airline"
    _description = 'airline'
    _rec_name = 'airline_id'

    airline_id =  fields.Char("Airline Name")
    flight = fields.Integer("Total Flight")
    country = fields.Char("Country Name")
    flight_ids = fields.One2many('flight','Aviation_id','Flight Name')