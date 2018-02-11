
from odoo import models, fields, _


class SaleOrder(models.Model):

    _inherit = "sale.order"

    location_signed_in = fields.Char(string=_(u'Місце складання'))