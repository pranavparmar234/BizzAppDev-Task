# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, _
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.constrains('name')
    def _unique_category_name(self):
        for category in self:
            if self.search([('name', '=', category.name)], limit=1) - category:
                raise ValidationError(_("The category %s must be unique!" % category.name))
