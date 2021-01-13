from odoo import models, fields, api, _
from odoo.exceptions import UserError
import math


class product_template(models.Model):
    _inherit = 'product.template'

    is_product_pack = fields.Boolean(string='Is Product Pack')

    pack_ids = fields.One2many('product.pack.lines', 'bundle_template_id','Budle Line')

    @api.constrains('is_product_pack')
    def check_pack_product(self):
        for rec in self:
            if rec.is_product_pack:
                if not rec.pack_ids:
                    raise UserError('Please Add Product Pack')
                if rec.lst_price == 0:
                    raise UserError('Sale Price can no be zero for Bundle Pack')

    def _compute_quantities(self):
        for rec in self:
            super(product_template,rec)._compute_quantities()
            if rec.is_product_pack:
                product_qunt_list = {}
                for pack in rec.pack_ids:
                    product_name = pack.product_id.name
                    qty = pack.product_qty
                    on_hand_qty = pack.qty_available
                    try:
                        total_quan = int(math.floor(on_hand_qty / qty))
                    except:
                        total_quan = 0
                    product_qunt_list[product_name] = total_quan
                try:
                    rec.qty_available = int(math.floor(min(product_qunt_list.values())))
                except:
                    rec.qty_available = False

    @api.onchange('pack_ids')
    def _get_combo_price(self):
        for rec in self:
            if rec.pack_ids:
                total_lst_price = 0
                for pack in rec.pack_ids:
                    total_lst_price += pack.product_qty * pack.product_id.lst_price
                self.list_price = total_lst_price    

    def action_open_quants(self):
        if self.is_product_pack:
            return True
        else:
            return super(product_template,self).action_open_quants()    
