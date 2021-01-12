

from odoo import models , fields ,api ,_

class partner_model(models.Model):
    _name = "partner.model"
    _description = 'partner model'
    _rec_name = 'address'
    
   
    address = fields.Char('Address')
    mo_number = fields.Char('Mo.number')
    is_customar = fields.Boolean('Customar')
    is_vendor = fields.Boolean('Vendor')
    image_file = fields.Binary('Image file')



  
   
   
   
    
