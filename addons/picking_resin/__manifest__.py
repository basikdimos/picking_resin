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

        'views/hr_employee_ext_view.xml',
        'views/hr_department_ext_view.xml',
        'views/work_shift_views.xml',
        'views/shift_employee_list_view.xml',

        'views/menus.xml',
    ],
    'demo': [],
    'application': True,
    'sequence': -100,
}