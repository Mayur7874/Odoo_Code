from odoo import models , fields ,api ,_
from odoo.exceptions import UserError


class customar_info_spt(models.Model):
    _name = "customar.info.spt"
    _description = 'customar info spt'
    _rec_name = 'cus_name'
    

    cus_name = fields.Char('Customat Name')
    cus_address = fields.Char('Customat Address')
    pur_category = fields.Selection([('grocery','Grocery'),('electronic','Electronic'),('food','Food'),('home_appliances','Home Appliances')], string='Purchase Product Category')
    # pur_name = fields.Char('Purchase Product Name')
    cur_to_productname_id = fields.Many2one('product.info.spt','Purchase Product Name')
    pur_product_company = fields.Char('Purchase Product Company Name')
    # Cur_to_pro_id = fields.Many2one('product.info.spt','Purchase Product Company Name')
    cus_sale_price = fields.Float('Product Cost', compute="_get_cus_sale_price")
    pur_date = fields.Datetime('Purchase Date')
    # cus_warranty_selection = fields.Boolean('Product Warranty')
    cus_pro_my = fields.Char('Product Warranty Month/Year', compute="_get_Pro_warranty")
    cus_pro_warranty_time = fields.Integer('Product Warranty Time')
    cus_to_pro_qun = fields.Integer('Total Quantity')
    state = fields.Selection([('draft','Draft'),('confirm','Confirm')],'State',default="draft")





     
    @api.onchange('cur_to_productname_id')  
    def pro_name_pro_cat(self):
        for rec in self:
            if rec.cur_to_productname_id:
                rec.pur_category = rec.cur_to_productname_id.pro_category
                

    @api.onchange('cur_to_productname_id')
    def pro_name_pro_company(self):
        for rec in self:
            if rec.cur_to_productname_id:
                rec.pur_product_company = rec.cur_to_productname_id.pro_company

    @api.depends('cur_to_productname_id','cus_to_pro_qun')
    def _get_cus_sale_price(self):
        for rec in self:
            s =  rec.cur_to_productname_id.pro_sale_price 
            p =  s * rec.cus_to_pro_qun
            rec.cus_sale_price  = p
        
    
         
    @api.onchange('cur_to_productname_id')  
    def pro_name_pro_wt(self):
        for rec in self:
                rec.cus_pro_warranty_time = rec.cur_to_productname_id.pro_warranty_time
                
         
    @api.onchange('cur_to_productname_id')  
    def _get_Pro_warranty(self):
        for rec in self:
                wa = rec.cur_to_productname_id.pro_my
                if wa:
                    rec.cus_pro_my = wa
                else:
                    rec.cus_pro_my = 0    
                

    # @api.onchange('cur_to_productname_id','cus_to_pro_qun')
    # def cus_qun_pro_qun(self):
    #     for rec in self:
    #         if rec.cus_to_pro_qun >= 0 and rec.cus_to_pro_qun <= rec.cur_to_productname_id.Pro_qun:
    #             Quantity = rec.cur_to_productname_id.Pro_qun
    #             Total = Quantity - rec.cus_to_pro_qun
    #             rec.cur_to_productname_id.write({'Pro_qun' : Total})

    #         elif rec.cus_to_pro_qun < 0:
    #             raise UserError(_('Please vaild number'))

    #         elif rec.cus_to_pro_qun > rec.cur_to_productname_id.Pro_qun:
    #             raise UserError(_('Stock is Not enough'))
                


    def update_confirm(self):
        for rec in self:
            if rec.cus_to_pro_qun >= 0 and rec.cus_to_pro_qun <= rec.cur_to_productname_id.Pro_qun:
                Quantity = rec.cur_to_productname_id.Pro_qun
                Total = Quantity - rec.cus_to_pro_qun
                rec.cur_to_productname_id.write({'Pro_qun' : Total})
                rec.state = 'confirm'
                

            elif rec.cus_to_pro_qun < 0:
                raise UserError(_('Please vaild number'))

            elif rec.cus_to_pro_qun > rec.cur_to_productname_id.Pro_qun:
                raise UserError(_('Stock is Not enough'))


    def category_wise_info(self):
        for rec in self:
            

            pro_obj = self.env['product.info.spt']

            c_id = rec.pur_category
            pro = pro_obj.search([('pro_category','=',c_id)])
            p_list = []

            for ids in pro:
                p_list.append(ids.id)

            return {
            'name' : _('product cat'),
            'domain' : [('id','in',p_list)],
            'res_model' : 'product.info.spt',
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',
            }    

    def com_wise_info(self):
        for rec in self:

            pro_obj = self.env['product.info.spt']

            cu_id = rec.pur_product_company
            pros = pro_obj.search([('pro_company','=',cu_id)])
            s_list = []

            for ids in pros:
                s_list.append(ids.id)

            return{
            'name' : _('product Name'),
            'domain' : [('id','in',s_list)],
            'res_model' : 'product.info.spt',
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',


            }






        
            
        

           
        
            # product_obj = self.env['product.info.spt']
            # s = product_obj.search([('id','=','1')]).Pro_qun
            # Total.write({'Pro_qun'})

           


    