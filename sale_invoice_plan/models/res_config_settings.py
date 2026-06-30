# Copyright 2026 Ctrl-a
# License AGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    auto_create_invoices_on_confirm = fields.Boolean(
        string="Create draft invoices on confirmation",
        config_parameter="sale_invoice_plan.auto_create_invoices_on_confirm",
        help="When enabled, all planned invoices will be automatically "
        "created as drafts when the sale order is confirmed.",
    )
