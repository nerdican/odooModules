AI Integration Module
=====================

This is a demonstration addon providing a basic framework to integrate
external AI services such as ChatGPT and Google Gemini with Odoo.

The module defines placeholder models, controllers and JavaScript
assets which can be extended for real integrations.

Requirements
------------

- The ChatGPT integration requires the ``openai`` and ``markdown`` Python
  packages.
- The Gemini integration requires ``google-generativeai``.
- Install the dependencies with::

      pip install openai markdown google-generativeai

- The Odoo modules **Live Chat** (``im_livechat``) and **Discuss** must be
  installed.
