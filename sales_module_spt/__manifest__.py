
{
    'name' : 'Sales Module',
    'version' : '13.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/partner_model_view.xml',        
        # 'views/sale_order_line_view.xml',

    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}