
{
    'name' : 'Inventory stock Valuation',
    'version' : '14.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['stock'],
    'data':[
        'security/ir.model.access.csv',
        'report/report _action_Inventory_stock_valuation_spt_view.xml',
        'report/report_template_Inventory_stock_valuation_spt_view.xml',
        'wizard/inventory_stock_valuation_wizard_spt_view.xml',    
        

    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}