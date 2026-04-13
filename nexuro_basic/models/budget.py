
from odoo import models, fields, api

class Budget(models.Model):
    _name = 'nexuro.budget'
    name = fields.Char(required=True)
    department = fields.Char()
    budget_amount = fields.Float()
    line_ids = fields.One2many('nexuro.budget.line','budget_id')
    spent_amount = fields.Float(compute="_compute_spent")
    remaining_amount = fields.Float(compute="_compute_remaining")

    @api.depends('line_ids.amount')
    def _compute_spent(self):
        for rec in self:
            rec.spent_amount = sum(l.amount for l in rec.line_ids)

    @api.depends('budget_amount','spent_amount')
    def _compute_remaining(self):
        for rec in self:
            rec.remaining_amount = rec.budget_amount - rec.spent_amount
