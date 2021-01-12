from odoo import models, fields, api, _
from odoo.exceptions import UserError


class book_food_beverage(models.Model):
    _name = "book.food.beverage"
    _description = 'book food beverage'

    item_id = fields.Many2one('food.beverage', 'Item')
    price = fields.Float('Price', related='item_id.price', store=True)
    quantity = fields.Integer('Qty', default=0)
    subtotal = fields.Float('Sub-Total', compute='get_price_total', store=True)
    rel_book_id = fields.Many2one('booking', 'book id')


    @api.depends('price','quantity')
    def get_price_total(self):
        self.subtotal = self.price * self.quantity

    