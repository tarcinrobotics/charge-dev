{
    'name': 'MuK Colors', 
    'summary': 'Customize your Nirvagi colors',
    'description': '''
        This module gives you options to customize the theme colors.
    ''',
    'version': '17.0.1.0.3', 
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'MuK IT',
    'website': 'https://tarcin.in',
    'live_test_url': 'https://tarcin.in',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'base_setup',
        'web_editor',
    ],
    'data': [
        'templates/webclient.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'muk_web_colors/static/src/scss/colors.scss'),
            (
                'before', 
                'muk_web_colors/static/src/scss/colors.scss', 
                'muk_web_colors/static/src/scss/colors_light.scss'
            ),
        ],
        'web.assets_web_dark': [
            (
                'after', 
                'muk_web_colors/static/src/scss/colors.scss', 
                'muk_web_colors/static/src/scss/colors_dark.scss'
            ),
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'uninstall_hook': '_uninstall_cleanup',
}
