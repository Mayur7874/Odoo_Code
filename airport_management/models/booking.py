from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, timedelta


class booking(models.Model):
    _name = "booking"
    _description = 'booking'

    ticket_id = fields.Char(
        "Ticket ID", default=lambda self: self.env['ir.sequence'].next_by_code('increment_ticket_id'))
    partner_id = fields.Many2one('res.partner', 'Name') 
    image =  fields.Binary('Image',related='partner_id.image_1920')
    date = fields.Date('Date')
    category = fields.Selection(
        [('national', 'National'), ('international', 'International')], string='Journey Category')
    routes_id = fields.Many2one('route', string='Route')
    booking_flight_id = fields.Many2one(
        'flight.schedule', string='Flight Name')
    comapny_id = fields.Many2one(
        'airline', 'Aviation Name', related='booking_flight_id.aviation_id')
    seat_category_id = fields.Many2one('seat.category', 'Seat Category')
    book_seats = fields.Integer('Total Seats')
    status = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'),
                               ('cancel', 'Cancel')], string="status", default='draft')

    boarding_time = fields.Datetime('Boarding Time')

    food_beverage_ids = fields.One2many(
        'book.food.beverage', 'rel_book_id', 'Food & Beverage')

    amount = fields.Float('Amount')
    food_beverage_charge = fields.Float('Food & Beverage Charge')
    net_amount = fields.Float('Total', compute='net_amount_total')

   

    @api.onchange('date')
    def date_onchange_field(self):
        current_date = date.today()
        if self.date:
            if current_date > self.date:
                raise UserError('All Flight has already booked')

    @api.onchange('category')
    def category_onchange_field(self):
        for rec in self:
            return{'domain': {'routes_id': [('category', '=', rec.category)]}}

    @api.onchange('date', 'category', 'routes_id')
    def flight_onchange_field(self):
        for rec in self:
            return {'domain': {'booking_flight_id': [('date', '=', rec.date), ('category', '=', rec.category), ('route_id', '=', rec.routes_id.id)]}}

    @api.onchange('booking_flight_id')
    def seat_category(self):
        if self.booking_flight_id:
            self.boarding_time = self.booking_flight_id.arrival_time + \
                timedelta(hours=-2)
            for rec in self:
                return {'domain': {'seat_category_id': [('category_flight_id', '=', rec.booking_flight_id.flight_id.id)]}}

    @api.onchange('book_seats')
    def book_seat(self):
        booking_obj = self.env['booking']
        # , ('book_seats', '=', self.book_seats)
        if self.book_seats:
            for rec in self:
                booking_lines = booking_obj.search([('booking_flight_id', '=', rec.booking_flight_id.id),
                                                    ('seat_category_id', '=', rec.seat_category_id.id), ('status', '=', 'confirm')])
                total_book_seat = 0
                for booking_line in booking_lines:
                    total_book_seat += booking_line.book_seats

                live_seat = total_book_seat + rec.book_seats

                if live_seat > rec.seat_category_id.total_seat:
                    raise UserError('Selected  Class Is Full.' + str(
                        rec.seat_category_id.total_seat - total_book_seat) + ' Seat Available')

    @api.onchange('book_seats')
    def amount_onchange(self):
        self.amount = self.seat_category_id.price * self.book_seats

    @api.onchange('food_beverage_ids')
    def food_beverage_charge_onchange_field(self):
        total = 0
        for food_beverage in self.food_beverage_ids:
            total += food_beverage.subtotal
        self.food_beverage_charge = total

    @api.depends('amount', 'food_beverage_charge')
    def net_amount_total(self):
        self.net_amount = self.amount + self.food_beverage_charge

    def action_confirm(self):
        self.status = 'confirm'

    def action_cancel(self):
        self.status = 'cancel'
  