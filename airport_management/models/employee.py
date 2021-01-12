from odoo import models, fields, api, _


class employee(models.Model):
    _inherit = 'hr.employee'

    employee_address = fields.Char('Address')
    employee_phone = fields.Char('Phone')
    employee_airline_id = fields.Many2one('airline','Airline')
    employee_flight_id = fields.Many2one('flight','Flight')
    employee_status =  fields.Boolean('Employess Status')

  