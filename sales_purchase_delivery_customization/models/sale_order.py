from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        super().action_confirm()
        for so in self:
            if so.tag_ids:
                so.picking_ids.write({'tag_ids': so.tag_ids.ids})
