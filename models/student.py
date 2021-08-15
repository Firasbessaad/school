from odoo import models, fields, api, _, exceptions, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_student = fields.Boolean(
        string='is student',
    )
    is_parent = fields.Boolean(
        string='is Parent',
    )
    grade_id = fields.Many2one(
        string='Grade',
        comodel_name='sc.grade',
        ondelete='restrict',
    )
    group_id = fields.Many2one(
        string='Grade',
        comodel_name='sc.grade',
        ondelete='restrict',
    )


