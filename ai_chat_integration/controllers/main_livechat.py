from odoo import http
from odoo.http import request

class AiChatLivechatController(http.Controller):
    @http.route('/ai_chat_integration/message', type='json', auth='public', website=True)
    def ai_livechat_message(self, message=None, **kwargs):
        """Intercept website livechat messages and open bot chat."""
        if not message:
            return {}

        bot_partner = request.env.ref('base.partner_root')
        user_partner = request.env.user.partner_id
        channel_model = request.env['mail.channel'].sudo()
        channel = channel_model.search([
            ('channel_type', '=', 'chat'),
            ('channel_partner_ids', 'in', [bot_partner.id]),
            ('channel_partner_ids', 'in', [user_partner.id]),
        ], limit=1)
        if not channel:
            channel = channel_model.create({
                'channel_partner_ids': [(6, 0, [bot_partner.id, user_partner.id])],
                'channel_type': 'chat',
                'name': 'AI Livechat',
            })

        channel.sudo().message_post(
            body=message,
            author_id=user_partner.id,
            message_type='comment',
            subtype_xmlid='mail.mt_comment'
        )
        return {'channel_id': channel.id}
