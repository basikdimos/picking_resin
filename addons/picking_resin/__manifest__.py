{
    'name': "Picking Resin",
    'summary': """ Picking Resin managment """,
    'description': """ Picking Resin business managent """,
    'author': "STiM Dev Company",
    'website':"None",
    'category':'STiM',
    'version':'14.0.0',
    'depends': ['base',
                'uom'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/work_type_data.xml',
        'views/work_types_view.xml',

        'views/work_types_menu.xml'],
    'demo': [],
    'application': True,
    'sequence': -100,
}