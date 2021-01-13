
{
    'name': 'Convert Purchase from Sales Order',
    'version': '14.0.0.1',
    'summary': '',
    'author': 'SnepTech',
    'license': 'AGPL-3',
    'website': 'https://sneptech.com/',
    'category': '',
    'description': """
    
                   """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'wizard/create_purchase_order_wizard_spt.xml',


    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
