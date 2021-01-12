from odoo import fields , models, api ,_

class product_quant(models.Model):
    _name = "product.quant"
    _description = "product quant"

    product_name_equ_name = fields.Many2one('equ.products','Product Name')
    serial_number = fields.Char("Serial Number",default = lambda self : self.env['ir.sequence'].next_by_code('serial_ref'))
    model = fields.Char('Product Model')
    comapny_name = fields.Char('Comapny Name')
    asign_by = fields.Char('Asign By')
    asign_date = fields.Date('Asign Date')
    product_quant_employee_name = fields.Many2one('equ.employee','employee Name')
    employee_post = fields.Char('Post')
    active_selection = fields.Boolean('Product Active')
    deactive_selection = fields.Boolean('Product Deactive')
    
    reason = fields.Char('Deactive Reason')
    state = fields.Selection([('draft','Draft'),('active','Active'),('deactive','Deactive')],'State',default="draft")



    @api.onchange('product_name_equ_name')
    def onchange_product_name_model_name(self):
        for rec in self:
            if rec.product_name_equ_name:
                rec.model = rec.product_name_equ_name.model_number
                rec.comapny_name = rec.product_name_equ_name.company_name
      
    @api.onchange('product_quant_employee_name')
    def onchange_product_quant_employee_name(self):
        for rec in self:
            if rec.product_quant_employee_name:
                rec.employee_post = rec.product_quant_employee_name.post

        
    def product_stock(self):
        for rec in self:
            Total = rec.product_name_equ_name.stock - 1
            rec.product_name_equ_name.write({'stock':Total})

 
       


