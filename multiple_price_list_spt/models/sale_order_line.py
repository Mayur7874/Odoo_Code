from odoo import models,fields,api,_
from datetime import datetime
from odoo.exceptions import UserError 

class sale_order_line(models.Model):
    _inherit = "sale.order.line"


    def prepare_new_price_list(self,price_list_item_id,new_unit_price):
        vals = { 'pricelist_id':price_list_item_id.pricelist_id.id,
                 'unit': 1,
                 'unit_price':new_unit_price,
                 'order_line_id':self.id,
                }
        return vals
            
    
    def check_date(self,price_list_item_id):
        if price_list_item_id.date_start and not price_list_item_id.date_end and price_list_item_id.date_start.date() <= self.order_id.date_order.date():
            return True
        if not price_list_item_id.date_start and price_list_item_id.date_end and price_list_item_id.date_end.date() >= self.order_id.date_order.date():
            return True
        if price_list_item_id.date_start and price_list_item_id.date_end and price_list_item_id.date_start.date() <= self.order_id.date_order.date() and price_list_item_id.date_end.date() >= self.order_id.date_order.date():
            return True       
        else:
            return False
    

    def apply_pricelist_action(self,price_list_date = True):
        self.ensure_one()
        new_prices_list_line = []
        prices_list_item_ids = self.env['product.pricelist.item'].search(['|','|','|',('applied_on','=','3_global'),('categ_id','=',self.product_id.categ_id.id),('product_tmpl_id','=',self.product_id.product_tmpl_id.id),('product_id','=',self.product_id.id)])
    
        for price_list_item_id in prices_list_item_ids:
            if price_list_item_id.date_start or price_list_item_id.date_end:
                price_list_date = self.check_date(price_list_item_id)
                
            if price_list_date == True and price_list_item_id.min_quantity <= self.product_uom_qty:
                price = self.product_id.list_price

                if price_list_item_id.compute_price in ['formula'] and price_list_item_id.base in ['standard_price']:
                    price = self.product_id.standard_price

                new_unit_price = price_list_item_id._compute_price(price = price, price_uom = self.product_uom, product = self.product_id, partner= self.order_id.partner_id)
                price_list_vals = self.prepare_new_price_list(price_list_item_id,new_unit_price)
                new_prices_list_line.append(price_list_vals)
               

                
        if new_prices_list_line:
            old_pricelist_wizard_ids = self.env['apply.pricelist.line.wizard.spt'].search([('order_line_id','=',self.id)])
            if old_pricelist_wizard_ids:
                old_pricelist_wizard_ids.unlink()

            self.env['apply.pricelist.line.wizard.spt'].create(new_prices_list_line)

            pricelist_wizard_ids = self.env['apply.pricelist.line.wizard.spt'].search([('order_line_id','=',self.id)])

            compose_form = self.env.ref("multiple_price_list_spt.apply_pricelist_wizard_form_view")
            return {
                'name': _('Pricelist'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'apply.pricelist.wizard.spt',
                'views': [(compose_form.id, 'form')],
                'view_id': compose_form.id,
                'target': 'new',
                'context': {'default_apply_pricelist_ids':[(6,0,pricelist_wizard_ids.ids)]},
            }
        
        else:
            raise UserError('Selected Product Is Not eligible For Priceslist')


