from odoo import fields, models, api, _
from odoo.exceptions import UserError


class merge_picking_orders_wizard_spt(models.TransientModel):
    _name = "merge.picking.orders.wizard.spt"

    pickings_ids = fields.Many2many(
        'stock.picking', 'stock_orders_rel', 'stock_id', 'order_id', 'Pickings orders')

    def validate_records_spt(self, operation_type, status, partner_id):
        if len(self.pickings_ids.ids) > 1:
            for pickings_id in self.pickings_ids:
                if pickings_id.state != 'done':
                    if pickings_id.state != 'cancel':
                        if pickings_id.picking_type_id == operation_type:
                            if pickings_id.state == status:
                                if pickings_id.partner_id == partner_id:
                                    pass
                                else:
                                    raise UserError(
                                        'Merging is only allowed on same partner')
                            else:
                                raise UserError(
                                    'Merging is only allowed on same picking State')
                        else:
                            raise UserError(
                                'Merging is only allowed on same picking types')
                    else:
                        raise UserError(
                            'Merging is not allowed on Cancel State')
                else:
                    raise UserError('Merging is not allowed on Done State')
        else:
            raise UserError('Merging is not allowed one records.')
        return True

    def action_merge_order(self):
        operation_type = self.pickings_ids[0].picking_type_id
        status = self.pickings_ids[0].state
        partner_id = self.pickings_ids[0].partner_id
        scheduled_date = self.pickings_ids[0].scheduled_date
        location_id = self.pickings_ids[0].location_id
        location_dest_id = self.pickings_ids[0].location_dest_id
        validate_records = self.validate_records_spt(operation_type, status, partner_id)
        if validate_records == True:
            orders_ids = []
            for picking_id in self.pickings_ids:
                orders_ids.append(picking_id.sale_id)
                picking_id.action_cancel()
            self.env['sale.order'].acton_merge_sale_orders(orders_ids)
