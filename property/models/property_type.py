# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PropertyType(models.Model):
    _name = 'property.type'
    _description = "Property Type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'

    # Fields
    code = fields.Char(string='Code', required=True, tracking=True)
    name = fields.Char(string='Name', required=True, tracking=True)
