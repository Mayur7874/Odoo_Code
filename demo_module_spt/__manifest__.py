
{
    'name' : 'Demo Module',
    'version' : '13.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['product','stock','sale','base','purchase','mrp','account'],
    'data':[
        'security/ir.model.access.csv',
        # 'data/action_print_sale_order_report_spt.xml'
        'report/report_action_sale_order_spt.xml',
        'report/report_template_sale_order_spt.xml',


        'wizard/order_data_view.xml',
        # 'wizard/sales_report_for_sales_person_wizard_spt.xml',
        'wizard/account_payment_register_view.xml',
        'views/demo_model_spt_view.xml',
        'views/product_template_view.xml',
        'views/product_product_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        # 'views/sale_order_line_view.xml',
        'views/purchase_order_view.xml',
        'views/account_move_view.xml',
        'views/account_move_line_spt_view.xml',
        # 'views/sale_advance_payment_inv_view.xml',
        # 'views/mrp_production_view.xml',
        
        

    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}