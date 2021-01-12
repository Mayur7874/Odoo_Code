from odoo import models, fields, api, _


class account_move(models.Model):
    _inherit = 'account.move'

    invoice_pay_data = fields.Datetime('Pay Date')

    sale_data_id = fields.Many2one('sale.order', string='Sale Data')

    sale_order_data_line_ids = fields.One2many(
        'account.move.line.spt', 'invoice_id')

    @api.model
    def create(self, vals):
        res = super(account_move, self).create(vals)
        res.invoice_pay_data = self._context.get('payment_date_spt')
        res.sale_order_data_line_ids = self._context.get('commission')
        return res

    # @api.onchange('sale_order_data_line_ids')
    # def sale_order_data_line_ids_onchange_field(self):
    #     if self.sale_order_data_line_ids :
    #         self.sale_order_data_line_ids.partner_id = self.partner_id.id
    #         self.sale_order_data_line_ids.subtotal = self.amount_total

    def action_invoice_register_payment(self):
        return self.env['account.payment']\
            .with_context(active_ids=self.ids, active_model='account.move', active_id=self.id,default_sale_commission_ids=self.sale_order_data_line_ids.ids)\
            .action_register_payment()
