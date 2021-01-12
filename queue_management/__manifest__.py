
{
    'name' : 'Queue Management',
    'version' : '13.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':[],
    'data':[
        'security/ir.model.access.csv',

        'wizard/show_user_info.xml',
        'wizard/show_cat_info.xml',
        'views/que_user_view.xml',
        'views/que_product_view.xml',
        'views/que_problam_view.xml',
        'views/que_employee_view.xml',
        'views/que_tokan_interface_view.xml',
        'views/counter_interface_view.xml',
        'views/display_interface_view.xml',
    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}