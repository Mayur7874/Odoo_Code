
from odoo import models, fields, api, _


class auto_sale_workflow_spt(models.Model):
    _name = 'auto.sale.workflow.spt'

    name = fields.Char(string='Name', required=True)
    payment_journal_id = fields.Many2one('account.journal',string ='Payment Journal',domain="[('type', 'in', ['bank', 'cash'])]")

    confirm_order = fields.Boolean('Confirm Order',default=True)
    validation_picking = fields.Boolean('Validation Picking')
    create_invoice = fields.Boolean('Create Invoice')
    confirm_invoice = fields.Boolean('Confirm Invoice')
    register_payment = fields.Boolean('Register Payment')
    force_inventory_available = fields.Boolean('Force Inventory Available')
    expected_days = fields.Integer(string='Expected Days')
    shipping_policy_spt = fields.Selection([('direct', 'As soon as possible'),('one','When all products are ready')],string="Shipping Policy")
    invoice_policy_spt = fields.Selection([('order','Ordered quantities'),('delivery','Delivered quantities')],string="Invoice Policy")
   

    @api.onchange('confirm_order')
    def value_false_all_field(self):
        if self.confirm_order == False:
            self.validation_picking = False
            self.create_invoice = False
            self.confirm_invoice = False
            self.register_payment = False

    
    @api.onchange('validation_picking')
    def value_true_on_one_field(self):
        if self.validation_picking == True:
            self.confirm_order = True
        if self.validation_picking == False:
            self.create_invoice = False
            self.confirm_invoice = False
            self.register_payment = False
       

    @api.onchange('create_invoice')
    def value_true_on_two_field(self):
        if self.create_invoice == True :
            self.confirm_order = True
            self.validation_picking = True
        if self.create_invoice == False:
            self.confirm_invoice = False
            self.register_payment = False
        if self.invoice_policy_spt:
            self.invoice_policy_spt = False

      

    @api.onchange('confirm_invoice')
    def value_true_on_three_field(self):
        if self.confirm_invoice == True:
            self.confirm_order = True
            self.validation_picking = True
            self.create_invoice = True
        if self.confirm_invoice == False:
            self.register_payment = False

    
    @api.onchange('register_payment')
    def value_true_on_all_field(self):
        if self.register_payment == True:
            self.confirm_order = True
            self.validation_picking = True
            self.create_invoice = True
            self.confirm_invoice = True
        if self.payment_journal_id:
            self.payment_journal_id = False
    
    
    
    @api.onchange('shipping_policy_spt')
    def set_expected_days(self):
        if self.shipping_policy_spt in ['direct',False]:
            self.expected_days = False
           
               

