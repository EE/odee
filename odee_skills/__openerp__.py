# -*- coding: utf-8 -*-
{
    'name': "Odee: Skills management",

    'summary': """Adds a new "Skills" tab to employee profile""",

    'description': """
        Adds a new "Skills" tab to employee profile
    """,

    'author': "Ludwik Trammer, Laboratorium EE",
    'website': "http://www.laboratorium.ee",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'hr',
    ],

    # always loaded
    'data': [
        'views/employee.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
