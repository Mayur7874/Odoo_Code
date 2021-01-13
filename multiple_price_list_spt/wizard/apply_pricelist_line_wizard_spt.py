from odoo import fields,models,api,_

class apply_pricelist_line_wizard_spt(models.TransientModel):
    _name = "apply.pricelist.line.wizard.spt"

    
    pricelist_id = fields.Many2one('product.pricelist',string='Pricelist')
    unit = fields.Float('Unit')
    unit_price = fields.Float('Unit price')
    order_line_id = fields.Many2one('sale.order.line','Sale order line')


    def apply_pricelist_wizard_action(self):
        self.order_line_id.price_unit = self.unit_price
        



