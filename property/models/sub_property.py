# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError


class SubProperty(models.Model):
    _name = 'sub.property'
    _description = "Sub Properties"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'
    _rec_name = 'name'

    # Get Journal items
    def _get_invoice_count(self):
            for rec in self:
                    count = self.env['account.move'].search_count([('invoice_line_ids.sub_property_ids', '=', rec.id)])
                    rec.invoice_count = count

    # Smart Button Function ( button Box Invoice)
    def open_invoice(self):
            return {
                    'name': 'Invoice',
                    'view_type': 'form',
                    'domain': [('invoice_line_ids.sub_property_ids', '=', self.id)],
                    'res_model': 'account.move',
                    'view_id': False,
                    'view_mode': 'tree,form',
                    'type': 'ir.actions.act_window',
            }


    name = fields.Char(string='Name', required=True)
    main_property_id = fields.Many2one(comodel_name="main.property",
                                       string="Main Property ID", required=True,
                                       tracking=True)
    property_type_id = fields.Many2one(comodel_name="property.type",
                                       string="Unit Type", required=True,tracking=True)
    contract_type = fields.Selection(string="Contract Type",
                                     selection=[('residential', 'Residential'), ('commercial', 'Commercial')],
                                     required=True, index=True, default='residential',
                                     tracking=True)
    unit_status = fields.Selection(string="Unit Status",
                                   selection=[('non_rented', 'Non Rented'),
                                              ('booked_up', 'Booked Up'), ('rented', 'Rented')],
                                   index=True, default='non_rented', readonly=False,
                                   tracking=True)
    unit_rent = fields.Float(string='Rent', default=0.00, tracking=True)
    active = fields.Boolean(string='Active', default=True)
    image = fields.Binary(string="Image")
    # Components
    count_room = fields.Integer(string='Rooms', default=0, tracking=True)
    count_council = fields.Integer(string='Councils', default=0, tracking=True)
    count_toilet = fields.Integer(string='Toilet', default=0, tracking=True)
    # Smart Button
    invoice_count = fields.Integer(string="Invoice Count", required=False, compute='_get_invoice_count')



    # Constrains Duplicate Name
    @api.constrains('sub_property_number')
    def _check_unique_num(self):
        nums_ids = self.search([]) - self
        value = [x.sub_property_number for x in nums_ids]
        if self.sub_property_number in value:
            raise ValidationError(_('sub Property %s is already Exist') % (self.sub_property_number))


