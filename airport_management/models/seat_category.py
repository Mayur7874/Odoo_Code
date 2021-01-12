from odoo import models , fields ,api ,_

class seat_category(models.Model):
    _name = "seat.category"
    _description = 'seat category'

    name = fields.Char('Class')
    category_flight_id = fields.Many2one('flight','Flight Name')
    category_company_id = fields.Many2one('airline','Airline Name',related='category_flight_id.Aviation_id',store=True)
    price =  fields.Float('Class Price')
    total_seat = fields.Integer('Total Seat')

