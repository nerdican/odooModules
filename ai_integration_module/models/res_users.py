from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    chatgpt_api_key = fields.Char(string='ChatGPT API Key')
    gemini_api_key = fields.Char(string='Gemini API Key')
