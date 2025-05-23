/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { jsonrpc } from "@web/core/network/rpc_service";
import { LivechatButton } from "@im_livechat/components/livechat_button/livechat_button";

patch(LivechatButton.prototype, "ai_livechat", {
    async _postMessage(message, options) {
        let result = await jsonrpc('/ai_livechat/message', {message});
        if (result && result.channel_id) {
            this.env.services.action.doAction({
                type: 'ir.actions.act_window',
                res_model: 'mail.channel',
                res_id: result.channel_id,
                target: 'new',
            });
        }
        return await this._super(message, options);
    },
});
