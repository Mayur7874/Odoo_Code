from odoo import models, fields, api, _
from odoo.exceptions import UserError


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    prospect_state = fields.Selection(
        [('prospectnew', 'New'), ('hold', 'Hold'), ('lost', 'Lost')], default='prospectnew')
    type = fields.Selection([
        ('prospect', 'Prospect'), ('lead', 'Lead'), ('opportunity', 'Opportunity')],
        index=True, required=True, tracking=15,
        default=lambda self: 'lead' if self.env['res.users'].has_group('crm.group_use_lead') else 'opportunity')

    def marks_as_lost(self):
        self.prospect_state = 'lost'
        self.active = False

    def find_lead(self, prospect):
        lead_email = prospect.email_from
        lead = self.env['crm.lead'].search([('email_from', '=', lead_email),('type','=','lead')])
        prospect_list = []
        if lead:
            prospect.unlink()
            prospect_list.append(lead)
        else:
            if prospect.type in ['prospect']:
                prospect.type = 'lead'
                prospect_list.append(prospect)

        return prospect_list

    def merge_to_lead(self,find_lead = False):
        crm_lead_obj = self.env['crm.lead']
        for prospect in self:
            if prospect.type in ['prospect']:
                if prospect.email_from is not False:
                    lead_ids = crm_lead_obj.search([('email_from', '=', prospect.email_from),('type', '=', 'lead')])
                    if lead_ids:
                        for lead_id in lead_ids:
                            lead_vals = {}
                            if not lead_id.partner_name and prospect.partner_name:
                                lead_vals['partner_name'] = prospect.partner_name
                            if not lead_id.street and prospect.street:
                                lead_vals['street'] = prospect.street
                            if not lead_id.street2 and prospect.street2:
                                lead_vals['street2'] = prospect.street2
                            if not lead_id.city and prospect.city:
                                lead_vals['city'] = prospect.city
                            if not lead_id.state_id and prospect.state_id.id:
                                lead_vals['state_id'] = prospect.state_id.id
                            if not lead_id.zip and prospect.zip:
                                lead_vals['zip'] = prospect.zip
                            if not lead_id.country_id and prospect.country_id.id:
                                lead_vals['country_id'] = prospect.country_id.id
                            if not lead_id.website and prospect.website:
                                lead_vals['website'] = prospect.website
                            if not lead_id.contact_name and prospect.contact_name:
                                lead_vals['contact_name'] = prospect.contact_name
                            if not lead_id.title and prospect.title:
                                lead_vals['title'] = prospect.title
                            if not lead_id.email_from and prospect.email_from:
                                lead_vals['email_from'] = prospect.email_from
                            if not lead_id.email_cc and prospect.email_cc:
                                lead_vals['email_cc'] = prospect.email_cc
                            if not lead_id.function and prospect.function:
                                lead_vals['function'] = prospect.function
                            if not lead_id.phone and prospect.phone:
                                lead_vals['phone'] = prospect.phone
                            if not lead_id.mobile and prospect.mobile:
                                lead_vals['mobile'] = prospect.mobile
                            if not lead_id.description and prospect.description:
                                lead_vals['description'] = prospect.description
                            lead_id.write(lead_vals)
                        if find_lead == True:
                            prospect_data = prospect.find_lead(prospect)
                            return prospect_data
                        prospect.unlink()
                    else:
                        if find_lead == True:
                            prospect_data = self.find_lead(prospect)
                            return prospect_data
                else:
                    if find_lead == True:
                        prospect_data = self.find_lead(prospect)
                        return prospect_data

            else:
                raise UserError(
                    'This Action Is Use Only On Prospects Type Data')
          

    def convert_to_lead(self,find_lead = False):
        if len(self) == 1:
            find_lead = True
        for prospect in self:
            prospects_to_lead = prospect.merge_to_lead(find_lead)

        if len(self) > 1:
            for prospect in self:
                try:
                    if prospect.type == 'prospect':
                        prospect.type = 'lead'
                except:
                    pass

        if len(self) == 1:
            lead = prospects_to_lead[0]
            return {
                'name': _('Lead '),
                'view_mode': 'form',
                'res_model': 'crm.lead',
                'res_id': lead.id,
                'view_id': self.env.ref('crm.crm_lead_view_form').id,
                'type': 'ir.actions.act_window',
            }

    def restore_prospects(self):
        self.prospect_state = 'prospectnew'
        self.active = True

    def marks_as_hold(self):
        self.prospect_state = 'hold'

    def marks_as_prospect(self):
        self.prospect_state = 'prospectnew'
