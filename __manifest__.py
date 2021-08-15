{
    'name': 'School',
    'version': '14.0.1.0.0',
    'author': 'Firas Bessaad',
    'website': 'http://www.bessaadFiras.com',
    'category': 'School Management',
    'license': "AGPL-3",
    'complexity': 'easy',
    'Summary': 'A Module For School Management',
    'images': ['static/description/icon.png'],
    'depends': ['base'],
    'data': ['security/security.xml',
             'security/ir.model.access.csv',
             'views/school_view.xml',
             'views/parent_view.xml',
             'views/student_view.xml',
             'menus.xml',
             ],
    'installable': True,
    'application': True
}
