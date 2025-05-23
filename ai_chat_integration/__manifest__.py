{
    'name': 'AI Chat Integration',
    'version': '1.0.0',
    'summary': 'Livechat integration with external AI services.',
    'author': 'Example',
    'license': 'AGPL-3',
    'depends': ['base', 'mail', 'im_livechat', 'mail_bot'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/res_users_view.xml',
        'views/ai_livechat_assets.xml',
        'data/ai_integration_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'ai_chat_integration/static/src/js/ai_integration.js',
        ],
        'website.assets_frontend': [
            'ai_chat_integration/static/src/js/ai_livechat.js',
        ],
    },
    'installable': True,
}
