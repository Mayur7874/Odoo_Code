from odoo import fields,models,api,_

class show_user_info(models.TransientModel):
    _name = 'show.user.info'


    name = fields.Char('Name')
    