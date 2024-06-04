{
    'name': 'Student Portal',
    'version': '1.0',
    'summary': 'A portal to display student data',
    'description': 'This module creates a portal to display student data from the student module.',
    'author': 'Tarcin Inc',
    'category': 'website',
    'depends': ['base', 'website', 'student'],
    'data': [
        'data/student_data.xml',
        'view/portal_templates.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
