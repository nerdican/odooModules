from odoo import http

class AiChatIntegrationController(http.Controller):
    @http.route('/ai_chat_integration/ping', auth='user')
    def ping(self, **kw):
        return 'pong'
