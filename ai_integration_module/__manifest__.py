{
    'name': 'AI Integration Module',
    'version': '1.0.0',
    'summary': 'Example integration of ChatGPT and Gemini APIs.',
    'description': 'Stubs for integrating external AI services with Odoo.',
    'author': 'Example',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/res_users_view.xml',
        'data/ai_integration_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ai_integration_module/static/src/js/ai_integration.js',
        ],
    },
    'installable': True,
}
