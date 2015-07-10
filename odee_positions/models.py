# -*- coding: utf-8 -*-

from openerp import models, fields


class Project(models.Model):
    _name = 'odee.project'

    name = fields.Char(required=True)


class EmployeePositions(models.Model):
    _name = 'odee.employee_position'

    name = fields.Char(required=True)
    project = fields.Many2one('odee.project', ondelete='cascade', required=True)
    date_from = fields.Date(required=True)
    date_to = fields.Date()
    employee = fields.Many2one('hr.employee', ondelete='cascade', required=True)
    responsibilities = fields.Text()
    skills = fields.Text()
    other = fields.Text()


class Employee(models.Model):
    _inherit = 'hr.employee'

    positions = fields.One2many('odee.employee_position', inverse_name='employee')
