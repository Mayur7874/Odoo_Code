from odoo import models, fields, api, _
from odoo.exceptions import UserError


class example_cus_pro_line(models.Model):
    _name = "example.cus.pro.line"
    _description = 'example cus pro line'

    item_id = fields.Many2one('example.product', 'Item')
    price = fields.Float('Price', related='item_id.price', store=True)
    quantity = fields.Integer('Qty', default=0)
    subtotal = fields.Float('Sub-Total', compute='get_price_total', store=True)
    rel_customar = fields.Many2one('example.customar', 'Customar ID')

    # @api.onchange('item_id')
    # def _get_price(self):
    #     for rec in self:
    #         rec.price = rec.item_id.price

    @api.depends('price', 'quantity')
    def get_price_total(self):
        for rec in self:
            rec.subtotal = rec.price * rec.quantity

    # @api.onchange('quantity')
    # def count_quantity(self):
    #     for rec in self:
    #         if rec.item_id:
    #             if rec.quantity > 0 and rec.quantity <= rec.item_id.stock:
    #                 pass

    #             elif rec.quantity <= 0:
    #                 raise UserError(_('Please vaild number'))

    #             elif rec.quantity > rec.item_id.stock:
    #                 raise UserError(_('Stock is Not enough'))



    @api.onchange('quantity')
    def count_quantity(self):
        for rec in self:
            if rec.item_id:
                total = 0
                for each in self:
                    if each.quantity > 0 and each.quantity <= rec.item_id.stock:
                        total += each.quantity

                    elif each.quantity <= 0:
                        raise UserError(_('Please vaild number'))

                    elif each.quantity > rec.item_id.stock:
                        raise UserError(_('Stock is Not enough'))

    
    