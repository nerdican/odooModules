# -*- coding: utf-8 -*-
import logging
import time
from odoo import models, fields, api, _

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    # TODO driver type so we can install several and tie a bot to it
    is_ai_bot = fields.Boolean(string="Is an AI-Bot")
    openai_api_key = fields.Char(required=False)
    openai_base_url = fields.Char(required=False)
    openai_model = fields.Char(required=False)
    openai_max_tokens = fields.Integer(required=False)
    openai_temperature = fields.Float(required=False)
    # ~ chat_method = fields.Selection(required=False)
    chat_system_message = fields.Text(required=False)
    openai_prompt_prefix = fields.Char(required=False)
    openai_prompt_suffix = fields.Char(required=False)
    openai_assistant_name = fields.Char(required=False)
    openai_assistant_instructions = fields.Text(required=False)
    openai_assistant_tools = fields.Json(required=False)
    openai_assistant_model = fields.Char(required=False)
    openai_assistant = fields.Char(required=False)
    llm_type = fields.Selection([], string="LLM Type", default=False)

    def run_ai_message_post(self, recipient, channel, author, message):
        """ Returns the form action URL, for form-based acquirer implementations. """
        if hasattr(self, '%s_run_ai_message_post' % self.llm_type):
            return getattr(self, '%s_run_ai_message_post' % self.llm_type)(recipient, channel, author, message)
        return False

    # ----------------------------------------------------------
    # OpenAI
    # ----------------------------------------------------------

    def openai_run_ai_message_post(self, recipient, channel, author, message):
        """Send a message to OpenAI and post the response on the channel."""
        try:
            import openai
        except Exception as exc:  # pragma: no cover - library missing during tests
            _logger.error("Unable to import openai library: %s", exc)
            return False

        api_key = recipient.openai_api_key or self.env['ir.config_parameter'].sudo().get_param('chat_ai_bot_common.openai_api_key')
        if not api_key:
            _logger.warning("Missing OpenAI API key for user %s", recipient.id)
            return False

        openai.api_key = api_key
        if recipient.openai_base_url:
            openai.base_url = recipient.openai_base_url

        messages = []
        if recipient.chat_system_message:
            messages.append({'role': 'system', 'content': recipient.chat_system_message})
        messages.append({'role': 'user', 'content': message})

        try:
            response = openai.ChatCompletion.create(
                model=recipient.openai_model or 'gpt-3.5-turbo',
                messages=messages,
                temperature=recipient.openai_temperature or 0.0,
                max_tokens=recipient.openai_max_tokens or None,
            )
            answer = response.choices[0].message['content']
        except Exception as exc:
            _logger.exception("OpenAI request failed: %s", exc)
            return False

        channel.with_user(recipient).message_post(
            body=answer,
            message_type='comment',
            subtype_xmlid='mail.mt_comment',
        )
        return True

    # ----------------------------------------------------------
    # Gemini
    # ----------------------------------------------------------

    def gemini_run_ai_message_post(self, recipient, channel, author, message):
        """Send a message to Google Gemini and post the response on the channel."""
        try:
            import google.generativeai as genai
        except Exception as exc:  # pragma: no cover - library missing during tests
            _logger.error("Unable to import google.generativeai library: %s", exc)
            return False

        icp = self.env['ir.config_parameter'].sudo()
        api_key = icp.get_param('googel_gemini_odoo_connector.gemini_api_key')
        model_name = icp.get_param('googel_gemini_odoo_connector.gemini_model')
        if not api_key or not model_name:
            _logger.warning("Gemini API not configured")
            return False

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name=model_name)

        try:
            res = model.generate_content(message)
            answer = getattr(res, 'text', False) or ''
        except Exception as exc:
            _logger.exception("Gemini request failed: %s", exc)
            return False

        channel.with_user(recipient).message_post(
            body=answer,
            message_type='comment',
            subtype_xmlid='mail.mt_comment',
        )
        return True
