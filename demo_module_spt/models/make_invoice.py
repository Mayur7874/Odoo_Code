from odoo import models, fields, api, _


class sale_advance_payment_inv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    date = fields.Datetime("Name")
    sale_order_id = fields.Many2one('sale.order', 'Sale')

    # @api.onchange('advance_payment_method')
    # def name_onchange_field(self):
    #     sol = self.env['sale.order'].browse(self._context.get('active_ids'))
    #     self.date = sol.payment_date

    # def create_invoices(self):
    #     if self.date:
    #         ctx = self._context.copy()
    #         ctx['payment_date_spt'] = self.date
    #         self = self.with_context(ctx)

    #     res = super(sale_advance_payment_inv, self).create_invoices()
    #     return res

    def create_invoices(self):
        sol = self.env['sale.order'].browse(self._context.get('active_ids'))
        ctx = self._context.copy()
        ctx['payment_date_spt'] = sol.payment_date
        ctx['total_amount'] = sol.amount_total
        ctx['commission'] = sol.commission_id
        self = self.with_context(ctx)

        res = super(sale_advance_payment_inv, self).create_invoices()
        return res
