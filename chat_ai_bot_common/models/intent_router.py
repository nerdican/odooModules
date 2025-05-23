import json
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class IntentRouter(models.AbstractModel):
    """Utility to classify incoming messages and route them to a channel."""

    _name = 'intent.router'
    _description = 'Intent Router'

    # ------------------------------------------------------------------
    # Intent classification
    # ------------------------------------------------------------------
    def classify_intent(self, message):
        """Return the intent label for the given message using Intent GPT."""
        api_key = self.env['ir.config_parameter'].sudo().get_param('chat_ai_bot_common.intent_gpt_api_key')
        model = self.env['ir.config_parameter'].sudo().get_param('chat_ai_bot_common.intent_gpt_model', default='gpt-3.5-turbo')
        if not api_key:
            return False

        try:  # pragma: no cover - third party libraries might be missing
            import openai
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{'role': 'user', 'content': message}],
                temperature=0,
            )
            return response.choices[0].message['content'].strip()
        except Exception as exc:
            _logger.exception("Intent classification failed: %s", exc)
            return False

    # ------------------------------------------------------------------
    # Routing
    # ------------------------------------------------------------------
    def route_message(self, visitor, message):
        """Route the visitor to a channel based on the classified intent."""
        intent = self.classify_intent(message)
        mapping_json = self.env['ir.config_parameter'].sudo().get_param('chat_ai_bot_common.intent_router_map')
        mapping = json.loads(mapping_json or '{}')

        channel = False
        if intent and intent in mapping:
            channel = self.env.ref(mapping[intent], raise_if_not_found=False)

        if not channel and 'default' in mapping:
            channel = self.env.ref(mapping['default'], raise_if_not_found=False)

        if channel:
            channel.sudo().message_post(
                body=message,
                author_id=visitor.id,
                message_type='comment',
                subtype_xmlid='mail.mt_comment',
            )
            return channel.id

        return False

