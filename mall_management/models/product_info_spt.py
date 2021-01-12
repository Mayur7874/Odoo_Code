from odoo import models , fields ,api ,_
from odoo.exceptions import UserError
from datetime import date

class product_info_spt(models.Model):
    _name = "product.info.spt"
    _description = 'product info spt'
    _rec_name = 'pro_name'

    pro_name = fields.Char('Product Name')
    pro_category = fields.Selection([('grocery','Grocery'),('electronic','Electronic'),('food','Food'),('home_appliances','Home Appliances')], string='Product.Category')
    pro_company = fields.Char('Company Name')
    pro_company_price = fields.Float('Product Amount')
    pro_sale_price = fields.Float('sale price')
    pro_incomeing_date = fields.Datetime('Product Date')
    pro_warranty_selection = fields.Boolean('Warranty')
    pro_my = fields.Selection([('month','Month'),('year','Year')], string='Warranty Month/Year')
    pro_warranty_time = fields.Integer('Warranty Time')
    Pro_sta_date = fields.Date('Product Made Date')
    Pro_exp_date = fields.Date('Product Expiry Date')
    Pro_qun = fields.Integer('Product quantity')
    active = fields.Boolean('Active')
    state = fields.Selection([('draft','Draft'),('archive','Archive')],'state',default="draft")
   #  date = fields.Date(string='date', default= lambda self:fields.Date.today())
    # emp = fields.Many2one('employee.info.spt','EMP')
    #  emp_address = fields.Char('Emp')

    # @api.onchange('pro_company_price')
    # def set_pro_sale(self):
    #     for rec in self:
    #         comp_price = rec.pro_company_price
    #         sale_price = comp_price + (comp_price * 20)/100
    #         rec.pro_sale_price = sale_price
   

   




    @api.onchange('pro_company_price','pro_category')
    def set_pro_sale(self):
        for rec in self:
            if rec.pro_category == 'grocery':
               comp_price = rec.pro_company_price
               sale_price = comp_price + (comp_price * 20)/100
               rec.pro_sale_price = sale_price
             
            elif rec.pro_category == 'electronic':
               comp_price = rec.pro_company_price
               sale_price = comp_price + (comp_price * 35)/100
               rec.pro_sale_price = sale_price

            elif rec.pro_category == 'food':
               comp_price = rec.pro_company_price
               sale_price = comp_price + (comp_price * 10)/100
               rec.pro_sale_price = sale_price
            
            elif rec.pro_category == 'home appliances':
               comp_price = rec.pro_company_price
               sale_price = comp_price + (comp_price * 30)/100
               rec.pro_sale_price = sale_price

            
   #  def update_quantity(self):
   #       for rec in self:
   #          if rec.Pro_qun <= 0:
   #             raise UserError(_('Please Udate Quantity'))
            # elif rec.Pro_qun < 0:
            #    raise UserError(_('Please vaild number'))
         
   
    def archive_to_show(self):
      for rec in self:
         rec.active = True
         rec.state = 'draft'

    def show_to_archive(self):
       for rec in self:
         if rec.Pro_exp_date == date.today():
            rec.active = False
            rec.state = 'archive'
              
           


    def pro_wise_info(self):
        for rec in self:
            

            cus_obj = self.env['customar.info.spt']

            p_id = rec.id
            cus = cus_obj.search([('cur_to_productname_id','=',p_id)])
            c_list = []

            for ids in cus:
                c_list.append(ids.id)

            return {
            'name' : _('customar'),
            'domain' : [('id','in',c_list)],
            'res_model' : 'customar.info.spt',
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',
            }    




   





    