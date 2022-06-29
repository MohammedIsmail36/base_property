# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import *


class MainProperty(models.Model):
    _name = 'main.property'
    _description = "Main Property"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # =====================
    # === SMART BUTTONS ===
    # =====================
    # Get Sub Property Count ( button Box sub Property)
    # ===================================================
    def _get_sub_property_count(self):
        for rec in self:
            count = self.env['sub.property'].search_count([('main_property_id', '=', rec.id)])
            rec.sub_property_count = count

    # Smart Button Function ( button Box sub Property)
    def open_sub_properties(self):
        return {
            'name': 'Sub Properties',
            'view_type': 'form',
            'domain': [('main_property_id', '=', self.id)],
            'res_model': 'sub.property',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }


    # Get Journal items
    def _get_journal_items(self):
        for rec in self:
            count = self.env['account.move.line'].search_count([('main_property_id', '=', rec.id)])
            rec.journal_items_count = count

        # Smart Button Function ( button Box sub Property)

    def open_journal_items(self):
        return {
            'name': 'Journal Items',
            'view_type': 'form',
            'domain': [('main_property_id', '=', self.id)],
            'res_model': 'account.move.line',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }







    #  Get Default Category
    def _default_category(self):
        return self.env['res.partner.category'].browse(self._context.get('category_id'))


    def sub_property_create_action(self):
        pass
    # ==============================  Fields ==============================
    # Main Fields
    name = fields.Char(string='Name', required=True, tracking=True)
    main_property_code = fields.Char(string='Code', required=False, copy=False,
                                     readonly=False, index=True, tracking=True)
    image = fields.Binary(string="Image", tracking=True)
    landlord = fields.Many2one(comodel_name="res.partner", string="Landlord", required=True, tracking=True)
    # Address & Main Information
    street = fields.Char(tracking=True)
    street2 = fields.Char(tracking=True)
    zip = fields.Char(change_default=True, tracking=True)
    city = fields.Char(tracking=True)
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]", tracking=True)
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', tracking=True)
    district = fields.Char(tracking=True)
    building_no = fields.Char(string='Building No', tracking=True)
    additional_no = fields.Char(string='Additional No', tracking=True)
    # ======
    # company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company, required=True,
    #                              tracking=True)
    # currency_id = fields.Many2one('res.currency', string='Currency', required=True, tracking=True)
    email = fields.Char(tracking=True)
    website = fields.Char('Website Link', tracking=True)
    category_id = fields.Many2many('res.partner.category', string='Tags', column1='partner_id',
                                   column2='category_id', default=_default_category, tracking=True)
    active = fields.Boolean(string='Active', default=True, tracking=True)
    # Page Responsible Fields
    contracts_officer = fields.Many2one(comodel_name="res.users", string="Contracts Officer",
                                        required=False, tracking=True)
    follow_up = fields.Many2one(comodel_name="res.users", string="Follow Up",
                                required=False, tracking=True)
    sub_property_ids = fields.One2many(comodel_name="sub.property",
                                       inverse_name="main_property_id", string="Sub Properties",
                                       copy=True, auto_join=True)
    # ==================================================================================
    # Smart Buttons Fields
    sub_property_count = fields.Integer(string="Sub Properties", required=False, compute='_get_sub_property_count')
    journal_items_count = fields.Integer(string="Journal Items", required=False, compute='_get_journal_items')


    # ========= CONSTRAINS ============
    _sql_constraints = [
        ('check_deposit', 'CHECK(deposit >= 0)', 'Warning: Deposit Area must be greater than zero'),
        (
        'check_deposit_returned', 'CHECK(deposit_returned >= 0)', 'Warning: Deposit Returned must be greater than zero')
    ]
    # Constrains Duplicate Name
    @api.constrains('name')
    def _check_unique_name(self):
        names_ids = self.search([]) - self
        value = [x.name.lower() for x in names_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(_('Warning: Main property is already Exist'))


# class CreateSubProperty(models.Model):
#     _name = 'sub.property.create'
#     _description = "create sub Property"
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#
# class PropertyType(models.Model):
#     _name = 'property.type'
#     _description = "Property Type"
#     _inherit = ['mail.thread', 'mail.activity.mixin']



