# -*- coding: utf-8 -*- 
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class AccountMove(models.Model):
    _inherit = "account.move"


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    main_property_id = fields.Many2one('main.property',store=True)
    sub_property_ids = fields.Many2many("sub.property", store=True, domain="[('main_property_id', '=', main_property_id)]",)


