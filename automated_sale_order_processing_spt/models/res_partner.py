from odoo import models, fields, api, _


class res_partner(models.Model):
    _inherit = 'res.partner'
    
    workflow_process_id = fields.Many2one(
        'auto.sale.workflow.spt', 'Workflow Process')
