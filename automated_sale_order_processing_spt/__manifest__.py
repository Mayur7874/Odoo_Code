
{
    'name': 'Automated Sale Order Processing',
    'version': '14.0.0.1',
    'summary': '',
    'sequence': 1,
    'author': 'Sneptech',
    'license': 'AGPL-3',
    'website': 'https://www.sneptech.com',
    'category': 'Sales',
    'description': """
    
                   """,
    'depends': ['stock', 'sale', 'account', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/action_auto_process_sale_order.xml',
        'security/autometed_sale_order_security.xml',
        'views/auto_sale_workflow_spt_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
