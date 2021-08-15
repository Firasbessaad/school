from odoo import models, fields, api, _, exceptions, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression

class AcademicYear(models.Model):
    '''Defines an academic year.'''

    _name = "sc.academic.year"
    _description = "Academic Year"
    _order = "sequence"

    sequence = fields.Integer('Sequence', required=True,
                              help="Sequence order you want to see this year.")
    name = fields.Char('Name', required=True, help='Name of academic year')
    code = fields.Char('Code', required=True, help='Code of academic year')
    date_start = fields.Date('Start Date', required=True,
                             help='Starting date of academic year')
    date_stop = fields.Date('End Date', required=True,
                            help='Ending of academic year')
    current = fields.Boolean('Current', help="Set Active Current Year")
    description = fields.Text('Description')

    period_ids = fields.One2many('sc.academic.period', 'year_id', 'Periods',
                                help="related Academic periods")

    @api.model
    def next_year(self, sequence):
        '''This method assign sequence to years'''
        year_id = self.search([('sequence', '>', sequence)], order='id',
                              limit=1)
        if year_id:
            return year_id.id
        return False

    def name_get(self):
        '''Method to display name and code'''
        return [(rec.id, ' [' + rec.code + ']' + rec.name) for rec in self]


    @api.constrains('date_start', 'date_stop')
    def _check_academic_year(self):
        '''Method to check start date should be greater than end date
           also check that dates are not overlapped with existing academic
           year'''
        new_start_date = self.date_start
        new_stop_date = self.date_stop
        delta = new_stop_date - new_start_date
        if delta.days > 365 and not calendar.isleap(new_start_date.year):
            raise ValidationError(_('''Error! The duration of the academic year
                                      is invalid.'''))
        if (self.date_stop and self.date_start and
                self.date_stop < self.date_start):
            raise ValidationError(_('''The start date of the academic year'
                                      should be less than end date.'''))
        for old_ac in self.search([('id', 'not in', self.ids)]):
            # Check start date should be less than stop date
            if (old_ac.date_start <= self.date_start <= old_ac.date_stop or
                    old_ac.date_start <= self.date_stop <= old_ac.date_stop):
                raise ValidationError(_('''Error! You cannot define overlapping
                                          academic years.'''))

    @api.constrains('current')
    def check_current_year(self):
        check_year = self.search([('current', '=', True)])
        if len(check_year.ids) >= 2:
            raise ValidationError(_('''Error! You cannot set two current year active!'''))


class AcademicPeriod(models.Model):
    '''Defines an academic period.'''

    _name = "sc.academic.period"
    _description = "Academic Period"
    _order = "sequence"

    sequence = fields.Integer('Sequence', required=True,
                              help="Sequence order you want to see this period.")
    name = fields.Char('Name', required=True, help='Name of academic period')
    code = fields.Char('Code', required=True, help='Code of academic period')
    date_start = fields.Date('Start Date', required=True,
                             help='Starting date of academic period')
    date_stop = fields.Date('End Date', required=True,
                            help='Ending of academic period')
    year_id = fields.Many2one('sc.academic.year', 'Academic Year', required=True,
                              help="Related academic year ")
    description = fields.Text('Description')

    _sql_constraints = [
        ('period_unique', 'unique(date_start, date_stop, year_id)',
         'Academic period should be unique!'),
    ]