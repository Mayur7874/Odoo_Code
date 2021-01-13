from odoo import models, fields, api, _
from odoo.exceptions import UserError
import math


class product_product(models.Model):
    _inherit = 'product.product'

    @api.constrains('is_product_pack')
    def check_pack_product(self):
        for rec in self:
            if rec.is_product_pack:
                if not rec.pack_ids:
                    raise UserError('Please Add Product Pack')

    def _compute_quantities(self):
        for rec in self:
            super(product_product,rec)._compute_quantities()
            if rec.product_tmpl_id.is_product_pack:
                product_qunt_list = {}
                for pack in rec.product_tmpl_id.pack_ids:
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

    def action_open_quants(self):
        if self.is_product_pack:
            return True
        else:
            return super(product_product,self).action_open_quants()            