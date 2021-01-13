from odoo import fields,models,api,_

class apply_pricelist_wizard_spt(models.TransientModel):
    _name = "apply.pricelist.wizard.spt"
    
    # apply_pricelist_ids = fields.One2many('apply.pricelist.line.wizard.spt','prices_list_wizard_id','Pricelist line')
    apply_pricelist_ids = fields.Many2many('apply.pricelist.line.wizard.spt','apply_prices_list_wizard_rel','apply_pricelist_wizard_id','apply_pricelist_wizard_line_id','Pricelist line')
    
   

    