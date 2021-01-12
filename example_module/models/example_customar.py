from odoo import models, fields, api, _


class example_customar(models.Model):
    _name = "example.customar"
    _description = 'example customar'

    name = fields.Char('Name')
    cus_pro_line_ids = fields.One2many('example.cus.pro.line', 'rel_customar')
    # cus_pro_line_ids = fields.Many2many('example.cus.pro.line', 'rel_customar','cus_id','pro_id','Customar')
    total = fields.Float('Total')

    @api.onchange('cus_pro_line_ids')
    def onchange_calculate(self):
        for rec in self:
            total = 0
            for each in rec.cus_pro_line_ids:
                total += each.subtotal
            rec.total = total


    def update_confirm(self):
        for rec in self:
            for each in rec.cus_pro_line_ids:
                Total = each.item_id.stock - each.quantity
                each.item_id.write({'stock':Total})
                

            # Quantity = rec.cur_to_productname_id.Pro_qun
            # Total = Quantity - rec.cus_to_pro_qun
            # rec.cur_to_productname_id.write({'Pro_qun' : Total}) 

