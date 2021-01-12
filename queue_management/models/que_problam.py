from odoo import models , fields ,api ,_


class que_problam(models.Model):
    _name = "que.problam"
    _description = "que problam"


    name = fields.Char('Problam Name')
    problem_pro_name = fields.Char('Product Name')
    problem_pro_model = fields.Char('Product Model Number') 