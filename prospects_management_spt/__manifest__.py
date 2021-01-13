
{
    'name': 'Prospects Management',
    'version': '14.0.0.1',
    'summary': '',
    'sequence': 1,
    'author': 'Sneptech',
    'license': 'AGPL-3',
    'website': 'https://www.sneptech.com',
    'category': 'Sales/CRM',
    'description': """
                   """,
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/action_convert_to_lead.xml',
        'data/action_merge_prospect_to_lead.xml',
        'views/crm_lead_view.xml',

    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
