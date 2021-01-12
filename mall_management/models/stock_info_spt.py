from odoo import models , fields ,api ,_


class stock_info_spt(models.Model):
    _name = "stock.info.spt"
    _description = 'stock info spt'


    name = fields.Char("Stock Product Name")
    exp_date = fields.Date("Stock Product Expiry Date")
    Pro_com = fields.Char('Stock Product CompanyName')