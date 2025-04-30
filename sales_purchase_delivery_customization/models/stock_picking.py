from odoo import models, fields, api
from lxml import etree


class StockPicking(models.Model):
    _inherit = "stock.picking"

    tag_ids = fields.Many2many(
        comodel_name='crm.tag',
        relation='stock_picking_tag_rel', column1='picking_id', column2='tag_id',
        string="Tags")
    tags_count = fields.Integer(compute="_compute_tags_count", string="Total Tags")

    def _compute_tags_count(self):
        for picking in self:
            picking.tags_count = len(picking.tag_ids)
