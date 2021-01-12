from odoo import models , fields ,api,_

class equ_products(models.Model):
    _name = "equ.products"
    _description = "equ products"


    name = fields.Char("Product Name")
    purches_date = fields.Date("Purches Date")
    model_number = fields.Char("Model Number")
    warranty_date = fields.Date("Warranty Date")
    company_name = fields.Char("Company Name")
    stock  = fields.Integer("Total Stock")


     
    def product_name_employee_name(self):
        for rec in self:
            

            product_quant_obj = self.env['product.quant']


            emp = product_quant_obj.search([('product_name_equ_name','=',rec.id)])
            emp_list = []

            for ids in emp:
                emp_list.append(ids.id)

            return {
            'name' : ('Employee'),
            'domain' : [('id','in',emp_list)],
            'res_model' : 'product.quant',
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',
            'context':{'search_default_product_name':1}
            }   
