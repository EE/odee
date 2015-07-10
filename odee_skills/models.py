# -*- coding: utf-8 -*-

from openerp import models, fields

LEVEL_CHOICES = [
    ('1', 'Basic'),
    ('2', 'Good'),
    ('3', 'Very Good'),
]


class Role(models.Model):
    _name = 'odee.employee_role'

    name = fields.Char(required=True)


class ProgrammingLanguage(models.Model):
    _name = 'odee.prog_language'

    name = fields.Char(required=True)


class Tool(models.Model):
    _name = 'odee.tool'

    name = fields.Char(required=True)


class EmployeeLanguage(models.Model):
    _name = 'odee.employee_language'

    language = fields.Many2one('odee.prog_language', ondelete='cascade', required=True)
    employee = fields.Many2one('hr.employee', ondelete='cascade', required=True)
    name = fields.Char(related='language.name')
    level = fields.Selection(LEVEL_CHOICES, required=True)


class EmployeeTool(models.Model):
    _name = 'odee.employee_tool'

    tool = fields.Many2one('odee.tool', ondelete='cascade', required=True)
    employee = fields.Many2one('hr.employee', ondelete='cascade', required=True)
    name = fields.Char(related='tool.name')
    level = fields.Selection(LEVEL_CHOICES, required=True)


class Employee(models.Model):
    _inherit = 'hr.employee'

    role = fields.Many2one('odee.employee_role')
    languages = fields.One2many('odee.employee_language', inverse_name='employee')
    tools = fields.One2many('odee.employee_tool', inverse_name='employee')
