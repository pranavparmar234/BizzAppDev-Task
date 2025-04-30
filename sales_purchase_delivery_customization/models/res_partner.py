from odoo import models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.depends('ref')
    def _compute_display_name(self):
        super()._compute_display_name()
        for partner in self:
            if partner.ref:
                partner.display_name = partner.name + f' [{partner.ref}]'
