{
    'name': "Picking Resin",
    'summary': """ Picking Resin managment """,
    'description': """ Picking Resin business managent """,
    'author': "STiM Dev Company",
    'website':"None",
    'category':'STiM',
    'version':'14.0.0',
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/test_views.xml',
        'views/hr_employee_ext_views.xml',
        'views/hr_department_ext_views.xml',

        'views/menus.xml',
    ],
    'demo': [],
    'application': True,
    'sequence': -100,
}