from odoo import models, fields, api, _
from odoo.exceptions import UserError


class account_move_line_spt(models.Model):
    _name = 'account.move.line.spt'
    
    sale_order_id = fields.Many2one('sale.order','Sale order') 

    partner_id = fields.Many2one('res.partner', 'Customer')

    invoice_id = fields.Many2one('account.move', 'Invoice')

    account_payment_id = fields.Many2one('account.payment', 'payment_id')

    payment_selection = fields.Selection(
        [('fixed', 'Fixed Amount'), ('percentage', 'Percentage Amount')])

    fixed_amount = fields.Float('Fixed')

    percentage_amount = fields.Float('percentage')

    subtotal = fields.Float('Subtotal')

    total = fields.Float('Total')

    order_name = fields.Char('Order name')
   

    @api.onchange('percentage_amount')
    def percentage_onchange_field(self):
        if self.percentage_amount:
            self.total = self.percentage_amount * self.subtotal / 100
            self.fixed_amount = self.total

    @api.onchange('fixed_amount')
    def fixed_amount_onchange_field(self):
        if self.fixed_amount:
            self.percentage_amount = self.fixed_amount * 100 / self.subtotal
            self.fixed_amount = self.total
     
  
    
    @api.onchange('payment_selection')
    def subtotal_onchange_field(self):
        if self.payment_selection:
            if self.subtotal == 0.0:
                raise UserError('Please add product')
    
    # @api.model
    # def m_unlink(self,lines):
       
    #     for line in lines:
    #         line.unlink()