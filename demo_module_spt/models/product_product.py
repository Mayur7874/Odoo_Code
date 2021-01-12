from odoo import models, fields, api, _


class product_product(models.Model):
    _inherit = 'product.product'

    # customer = fields.Many2one("res.partner", "Customer")

    # partner_ids = fields.Many2many('res.partner', 'pro_pro_partner_rel_spt', 'pro_pro_id', 'partner_id', string='Partners',compute='get_partner_ids')
    partner_ids = fields.One2many('sale.order.line', 'product_id', 'Partner')
    # partner_ids = fields.Many2one('sale.order.line', 'Partner')
    

    # customer = fields.Many2many('res.partner', 'pro_pro_partner_rel_spt', 'pro_pro_id', 'partner_id', string='Partners',compute='get_partner_ids',)

    # @api.depends()
    # def get_partner_ids(self):
    #     for rec in self:
    #         sale_order_line_obj = self.env['sale.order.line']
    #         sale_order_lines = sale_order_line_obj.search([('product_id','=',rec.id)])

    #         sale_order_obj = self.env['sale.order']
    #         t2 = sale_order_obj.search([('partner_id','=',rec.id)])


    #         for ids in t2:
    #             if(ids.partner_id.name == rec.partner_ids)





