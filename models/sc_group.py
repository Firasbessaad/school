from odoo import models, fields, api, _, exceptions, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

class Gruop(models.Model):
    ''' Defining a Group'''

    _name = "sc.group"
    _description = "Group"
    _order = "sequence"

    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    description = fields.Text('Description')
    grade_id = fields.Many2one(
        string='Grade',
        comodel_name='sc.grade',
        ondelete='restrict',
    )
