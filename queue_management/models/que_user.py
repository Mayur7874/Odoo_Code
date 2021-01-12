from odoo import models , fields ,api ,_

class que_user(models.Model):
    _name = "que.user"
    _description = 'que user'
    

    name = fields.Char("Name")
    contact = fields.Char("Contact Number")  
    email = fields.Char('Email id') 
    bill_no = fields.Char('Bill No')
    tv = fields.Boolean("TV")
    phone = fields.Boolean("Phone")
    laptop = fields.Boolean("Laptop")
    use_to_product_rel = fields.Many2many('que.product','user_model_rel','use_id','model_id','Model Selection')
    use_to_probalm_rel = fields.Many2many('que.problam','user_problam_rel','user_id','problam_id','Probalm Selection')
    warrenty = fields.Selection([('active','Active'),('deactive','Deactive')],string="Warrenty Selection")
    rating = fields.Char("user Rating")
    status = fields.Selection([('submit','Submit Information'),('done','DONE')],'information Status',default="submit")

    names = fields.Char('product Name')


    @api.model  
    def create(self,vals):
        res = super(que_user,self).create(vals)
        res.email = 'abc@gmail.com'
        res.rating = '3'
        return res

    def write(self,vals):
        if not self.email:
            vals['email'] = 'aa'
        res = super(que_user,self).write(vals)    
        
        return res

    def unlink(self):
        self.use_to_product_rel.unlink()

        return super(que_user,self).unlink() 


    @api.onchange('phone','laptop','tv')
    def Phone_model(self):
        tol_obj = self.env['que.product']
        for rec in self:
            allow_ids = []
            if rec.phone == True:
                Phone_ids = tol_obj.search([('category','=','phone')])
                allow_ids = allow_ids + Phone_ids.ids
            if rec.laptop == True:
                Laptop_ids = tol_obj.search([('category','=','laptop')])
                allow_ids = allow_ids + Laptop_ids .ids
            if rec.tv == True:
                tv_ids = tol_obj.search([('category','=','tv')])
                allow_ids = allow_ids + tv_ids.ids
            return  {'domain': {'use_to_product_rel' : [('id','in',allow_ids)]}}



    def submit_info(self):
        for rec in self:
            tokan_obj = self.env['que.tokan.interface']
            tokan_obj.create({'username':rec.name,'usercontact': rec.contact,'tokan_model_rel':rec.use_to_product_rel,'tokan_Problam_rel':rec.use_to_probalm_rel})
            rec.status = 'done' 