from odoo import models, fields, api, _, exceptions, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


class Grade(models.Model):
    ''' Defining a Grade'''

    _name = "sc.garde"
    _description = "Garde"
    _order = "sequence"

    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    description = fields.Text('Description')
