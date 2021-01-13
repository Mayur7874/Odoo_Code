# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Multiple Price List',
    'version' : '14.0',
    'summary': 'Sale Order Multiple Pricelist',
    'sequence': 1,
    'description': """
    """,
    'category': 'Sale Order',
    'depends' : ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/apply_pricelist_wizard_view_spt.xml',
        'wizard/apply_pricelist_line_wizard_spt.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}