from odoo import models , fields ,api ,_


class food_beverage(models.Model):
    _name = "food.beverage"
    _description = 'food beverage'

    name = fields.Char('Food Name')
    price = fields.Float('Product Amount')
