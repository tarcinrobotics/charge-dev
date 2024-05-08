# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'TarcinBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add Tarcinbot in discussions',
    'website': 'https://tarcin.in',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mail_bot/static/src/scss/odoobot_style.scss',
        ],
    },
    'license': 'LGPL-3',
}
