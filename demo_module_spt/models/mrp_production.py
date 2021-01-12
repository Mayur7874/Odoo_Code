from odoo import models, fields, api, _


class mrp_production(models.Model):
    _inherit = 'mrp.production'

    # row_product_ids = fields.One2many('stock.move', 'raw_material_production_id','Row Product')


    def action_done(self):
        self.action_confirm()
        self.action_assign()
        self.open_produce_product()
        action = self.env['mrp.product.produce'].create({'production_id':{'product_id':self.product_id,'qty_producing':self.product_qty,'raw_workorder_line_ids':self.move_raw_ids}})
        action.do_produce()
        
    

         
