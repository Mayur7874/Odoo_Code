
{
    'name' : 'Equipment Management',
    'version' : '13.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['product','sale','account','base','mall_management','stock'],
    'data':[
        'security/ir.model.access.csv',
        'views/equ_products_view.xml',
        'views/product_quant_view.xml',
        'views/equ_employee_view.xml',
        'views/equ_request_view.xml',
        'views/product_template_view.xml',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/stock_info_spt_view.xml',
        # 'views/res_config_settings_view.xml',
        
    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}