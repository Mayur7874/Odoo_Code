from odoo import models, fields, api, _


class product_template(models.Model):
    _inherit = 'product.template'

    # total_stock = fields.Text()
    hand = fields.Float('On Hand', compute="depends_on_hand_stock")
    # mm_variant = fields.Many2many('product.product', 'product_variant_rel', 'product_id', 'variant_id', 'Variant')
    pro_varient = fields.One2many('product.product','product_tmpl_id','Product Varient')





    @api.depends('qty_available')
    def depends_on_hand_stock(self):
        for rec in self:
            rec.hand = rec.qty_available
            

    # @api.depends('name')
    # def depends_variant(self):
    #     for rec in self:
    #         return {'domain':['product_tmpl_id','=', id]}
     
    # @api.onchange('product_variant_count')
    # def depends_variant(self):    
    #     for rec in self: 
    #         rec.mm_variant = rec.product_variant_count.product_template_attribute_value_ids
                
                
  
       