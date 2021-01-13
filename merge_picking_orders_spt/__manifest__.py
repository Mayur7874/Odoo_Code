
{
    'name' : 'Merge Picking Orders Spt',
    'version' : '14.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['stock','sale'],
    'data':[
        'security/ir.model.access.csv',
        'data/action_merge_picking_orders_spt.xml',
        'wizard/merge_picking_orders_wizard_spt.xml',
        'views/sale_order_view.xml'
        

    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}