# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import fields, models, api


# 3 :  imports of odoo modules

# 4 :  imports from custom modules


_logger = logging.getLogger(__name__)


class OdooClassName(models.Model):
    """
    Work types dictionary.
        Fields:
            id / work_types / measure_unit
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'picking_resin.work_types'
    _description = 'Work types model'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration

    active = fields.Boolean(
        'Active',
        default=True
    )

    name = fields.Char(
        string="Work type",
        required='True'
    )

    measure_unit = fields.Many2one(
        string="UoM",
        comodel_name="uom.uom",
        required=True
    )

    # ------------------------------------------------------------------------------------------------------------------

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Selection method (methods used to return computed values for selection fields)

    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods

    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # And finally, other business methods.

    # ------------------------------------------------------------------------------------------------------------------