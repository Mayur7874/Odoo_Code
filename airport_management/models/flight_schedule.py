from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class flight_schedule(models.Model):
    _name = "flight.schedule"
    _description = 'flight schedule'
    _rec_name = 'flight_id'

    date = fields.Date('Schedule Date')
    flight_id = fields.Many2one('flight', string='Flight Name')
    aviation_id = fields.Many2one('airline','Aviation Name')
    route_id = fields.Many2one('route', string='Flight Route')
    gate_id = fields.Many2one('gate', string='Gate')
    arrival_time = fields.Datetime('Arrival Time')
    departure_time = fields.Datetime('Departure Time')
    category = fields.Selection(
        [('national', 'National'), ('international', 'International')], string='Flight Category')




    @api.onchange('flight_id')
    def route_onchange_field(self):
        self.route_id = self.flight_id.flight_route_id
        self.aviation_id = self.flight_id.Aviation_id.id
        self.category = self.flight_id.category
        return{'domain': {'gate_id': [('category', '=', self.flight_id.category)]}}


    @api.onchange('arrival_time')
    def departure_onchange_field(self):
        if self.arrival_time:
            self.departure_time = self.arrival_time + timedelta(hours=2)
            self.date = self.arrival_time.date()

    @api.onchange('gate_id')
    def time_onchange_field(self):
        flight_schedule_obj = self.env['flight.schedule']
        for rec in self:
            flight_schedule_lines = flight_schedule_obj.search([('date', '=', rec.date), ('gate_id', '=', rec.gate_id.id)])
            for flight_schedule_rec in flight_schedule_lines:
                if flight_schedule_rec.arrival_time <= rec.arrival_time < flight_schedule_rec.departure_time:
                    raise UserError('Gate is already scheduled')
