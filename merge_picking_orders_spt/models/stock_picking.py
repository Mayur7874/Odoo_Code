
from odoo import models, fields, api, _


class stock_picking(models.Model):
    _inherit = 'stock.picking'


    def action_merge_picking_orders(self):
        picking_ids = []
        for picking in self:
            picking_ids.append(picking.id)
        return {
            'name': _('Merge Picking'),
            'view_mode': 'form',
            'res_model': 'merge.picking.orders.wizard.spt',
            'type': 'ir.actions.act_window',
            'context': {'default_pickings_ids':[(6,0,picking_ids)]},
            'target': 'new',
        }

