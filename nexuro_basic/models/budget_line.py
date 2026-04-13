from odoo import models, fields

class BudgetLine(models.Model):
    _name = 'nexuro.budget.line'

    budget_id = fields.Many2one('nexuro.budget', ondelete='cascade')
    date = fields.Date()
    description = fields.Char()
    amount = fields.Float()

    # Campo nuevo para adjuntar PDF
    attachment = fields.Binary(string="Documento Adjunto")
    attachment_name = fields.Char(string="Nombre del Archivo")
