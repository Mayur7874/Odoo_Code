from odoo import models, fields, api, _
from odoo.exceptions import UserError


class sale_order(models.Model):
    _inherit = 'sale.order'

    def calculate_price_unit(self,bundle):
        self.ensure_one()
        price_dict = {}
        calculated_price = 0
        for pack in bundle.product_id.pack_ids:
            calculated_price += pack.product_id.lst_price * pack.product_qty
        if calculated_price != bundle.price_unit:
            if calculated_price > bundle.price_unit:
                diff_price = calculated_price - bundle.price_unit
                try:
                    diff_percent = (diff_price * 100)/calculated_price
                except:
                    diff_percent = 0
                for pack in bundle.product_id.pack_ids:
                    # price_dict[pack.product_id] = pack.product_id.lst_price - (pack.product_id.lst_price * diff_percent)/100
                    price_dict[pack.product_id] = pack.product_id.lst_price
                    price_dict['discount'] = diff_percent
            else:
                raise UserError("Pack's Unit Price can not be bigger than origin combo price")
                # diff_price = bundle.price_unit - calculated_price
                # try:
                #     diff_percent = (diff_price * 100)/calculated_price
                # except:
                #     diff_percent = 0
                # for pack in bundle.product_id.pack_ids:
                #     price_dict[pack.product_id] = pack.product_id.lst_price + (pack.product_id.lst_price * diff_percent)/100
        else:
            for pack in bundle.product_id.pack_ids:
                price_dict[pack.product_id] = pack.product_id.lst_price
                price_dict['discount'] = 0
        return price_dict        

    def _extract_bundle_pack(self,bundle_dict,order_dict):
        self.ensure_one()
        vals = []
        if bundle_dict:
            for bundle in bundle_dict.values():
                section = {
                    'order_id' : self.id,
                    'name' : str(bundle.product_id.name) + ' - ' + str(bundle.price_unit),
                    'salesman_id' : self.user_id.id,
                    'company_id' : self.company_id.id,
                    'order_partner_id' : self.partner_id.id,
                    'state' : 'draft',
                    'display_type' : 'line_section',
                    # 'qty_delivered_method' : 'manual',
                    # 'invoice_status' : 'no',
                }
                vals.append(section)
                price_dict = self.calculate_price_unit(bundle)
                for pack in bundle.product_id.pack_ids:
                    discount = price_dict['discount']
                    unit_price = price_dict[pack.product_id] if price_dict[pack.product_id] else 0
                    if unit_price == 0:
                        discount = 0
                    order_line = {
                        'order_id' : self.id,
                        'name' : pack.product_id.name,
                        'price_unit' : unit_price,
                        'product_id' : pack.product_id.id,
                        'product_uom_qty' : pack.product_qty * bundle.product_uom_qty,
                        'salesman_id' : self.user_id.id,
                        'tax_id' : bundle.tax_id.ids if bundle.tax_id else False,
                        'discount' : discount,
                        'company_id' : self.company_id.id,
                        'order_partner_id' : self.partner_id.id,
                        'qty_delivered_method' : 'stock_move',
                        'state' : 'draft',
                        # 'price_subtotal' : 100,
                        # 'invoice_status' : 'no',
                    }
                    vals.append(order_line)
        if order_dict:
            section = {
                    'order_id' : self.id,
                    'name' : 'Other Products',
                    'salesman_id' : self.user_id.id,
                    'company_id' : self.company_id.id,
                    'order_partner_id' : self.partner_id.id,
                    'state' : 'draft',
                    'display_type' : 'line_section',
                    # 'qty_delivered_method' : 'manual',
                    # 'invoice_status' : 'no',
                }
            vals.append(section)
            for order in order_dict.values():
                order_line = order.read()[0]
                for key,value in order_line.items():
                    if isinstance(value,tuple):
                        order_line[key] = value[0]
                vals.append(order_line)
        if vals:
           self.order_line.unlink()
           self.env['sale.order.line'].create(vals)
           super(sale_order,self).action_confirm()

    def action_confirm(self):
        self.ensure_one()
        bundle_dict = {}
        order_dict = {}
        for line in self.order_line:
            if line.product_id:
                if line.product_id.is_product_pack:
                    bundle_dict[line.id] = line
                else:
                    order_dict[line.id] = line
        if bundle_dict:
            self._extract_bundle_pack(bundle_dict,order_dict)
        else:
            super(sale_order,self).action_confirm()