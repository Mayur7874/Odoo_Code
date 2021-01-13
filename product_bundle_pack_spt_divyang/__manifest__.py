
{
    'name': 'Product Bundle Pack Spt',
    'version': '14.0.0.1',
    'summary': '',
    'author': 'SnepTech',
    'license': 'AGPL-3',
    'website': 'https://sneptech.com/',
    'category': '',
    'description': """
                   """,
    'depends': ['stock','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_pack_lines.xml',
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/sale_order_view.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
