# -*- coding: utf-8 -*- 
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class AccountMove(models.Model):
    _inherit = "account.move"

    # is_petty_cash = fields.Boolean(string="Is Petty Cash")
    # is_petty_expense = fields.Boolean(string="Is Petty Expenses")
    # petty_cash_id = fields.Many2one('petty.cash.expense.accounting', string="Petty Cash Id")
    # expense_id = fields.Many2one('expense.accounting.petty', string="Expense Id")
    #
    # #override to used pass refrence to jounral entry
    # @api.model
    # def create(self, vals):
    #     res = super(AccountMove, self).create(vals)
    #     if res.petty_cash_id:
    #         res.update({'ref' : res.petty_cash_id.name})
    #     return res
    #
    #
    # # override write method
    # def write(self, values):
    #     res = super(AccountMove, self).write(values)
    #     #for rec in self:
    #     #    #if ((rec.is_petty_expense and rec.expense_id) or (rec.is_petty_cash and rec.petty_cash_id)) and not self.env.context.get('from_petty'):
    #     #    #    raise UserError(_("Sorry! You Can't Edit Petty Cash Move"))
    #     return res
    #
    #
    # def button_cancel(self):
    #     for rec in self:
    #         if ((rec.is_petty_expense and rec.expense_id) or (rec.is_petty_cash and rec.petty_cash_id)) and not self.env.context.get('from_petty'):
    #             raise UserError(_("Sorry! You Can't Edit Petty Cash Move"))
    #     return super(AccountMove, self).button_cancel()

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    main_property_id = fields.Many2one('main.property',store=True)
    sub_property_ids = fields.Many2many("sub.property", store=True, domain="[('main_property_id', '=', main_property_id)]",)


