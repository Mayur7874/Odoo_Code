
{
    'name' : 'Airport Module',
    'version' : '13.0.0.1',
    'summary':'',
    'author':'SnepTech',
    'license':'AGPL-3',
    'website':'https://sneptech.com/',
    'category':'',
    'description': """
    
                   """,
    'depends':['hr'],
    'data':[
        'security/ir.model.access.csv',
        'views/flight_schedule_view.xml',
        'views/airline_view.xml',       
        'views/flight_view.xml',  
        'views/flight_view.xml',
        'views/route_view.xml',
        'views/gate_view.xml',
        'views/booking_view.xml',
        'views/seat_category_view.xml',
        'views/food_beverage_view.xml',
        'views/book_food_beverage_view.xml',
        'views/employee_view.xml',
    ],
    
    'application':True,
    'installable':True,
    'auto_install':False,
}