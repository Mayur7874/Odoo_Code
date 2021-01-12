from odoo import fields, models, api, _


class show_cat_info(models.TransientModel):
    _name = "show.cat.info"

    cat = fields.Char('Category')


    # def action_show_cato(self):
    #     for rec in self:
    #         pro_obj = self.env['que.product']

    
