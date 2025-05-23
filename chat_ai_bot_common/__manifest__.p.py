##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2024- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Chat AI-Bot: Common',
    # #if VERSION >= "17.0"
    'version': '1.4',
    # #elif VERSION == "16.0"
    'version': '1.3',
    # #endif
    'summary': 'Make OdooBot finally useful. Create users that you chat with just like ChatGPT. Integrate with OpenAI ChatGPT (GPT-3) or other LLM',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity / Discuss',
    'description': """
    Make OdooBot useful by adding OpenAI GPT intelligence.
    """,
    #'sequence': '1',
    'author': 'Vertel AB',
    'website': 'https://vertel.se/apps/odoo-ai/chat_ai_bot_common',
    'images': ['static/description/banner.png'], # 560x280 px.
    'license': 'AGPL-3',
    'contributor': '',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-ai',
    # Any module necessary for this one to work correctly
    'depends': [
        'mail',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/res_users.xml',
        'views/openai_log.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
