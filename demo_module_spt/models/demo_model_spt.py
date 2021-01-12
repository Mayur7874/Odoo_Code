

from odoo import models , fields ,api ,_

class demo_model_spt(models.Model):
    _name = "demo.model.spt"
    _description = 'Demo Model'
    
    name = fields.Char('Name')
    amount = fields.Float('Amount')
    num = fields.Integer('Number')
    date = fields.Date('Date')
    datetime = fields.Datetime('Datetime')
    show = fields.Boolean('Show')
    add_file = fields.Binary('File')
    select = fields.Selection([('abc','ABC'),('xyz','XYZ')], string='Select')


    
    location_id = fields.Many2one(string='Location', comodel_name='stock.location')
    id_company =  fields.Many2one('res.company', string='Comapny')
    
    ids_warehouses = fields.Many2many('stock.warehouse' , 'war_comapny_rel' , 'warehouses_id','com_id','Warehouse')
    Category_ids = fields.Many2many('product.category','product_category_rel','product_id','category_id','Category')


   
    