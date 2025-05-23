from odoo import http

class AiIntegrationController(http.Controller):
    @http.route('/ai_integration_module/ping', auth='user')
    def ping(self, **kw):
        return 'pong'
