from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pformat


class sale_order(models.Model):
    _inherit = 'sale.order'

    select_purchase = fields.Boolean('purchase order')
    def action_purchase_from_sale_order(self):
        self.select_purchase = True
        return {
            'name': _('Create Purchase Order'),
            'view_mode': 'form',
            'res_model': 'create.purchase.order.wizard.spt',
            'type': 'ir.actions.act_window',
            'context': {'default_sale_order_lines_ids': [(6, 0,self.order_line.ids)],
                        'default_partner_id':self.partner_id.id},
            'target': 'new',
        }
