# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import api, fields, models, _


# 3 :  imports of odoo modules

# 4 :  imports from custom modules


_logger = logging.getLogger(__name__)


class WorkShift(models.Model):
    """ 
    Регистрация факта
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'picking_resin.work_shift'
    _description = 'Picking Resin work shift'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Many2one(
        comodel_name= 'hr.department',
        string='District',
        required=True,
    )

    shift_date = fields.Datetime(
        string='Shift Date',
        required=True,
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Selection method (methods used to return computed values for selection fields)
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    @api.onchange('name')
    def _onchange_department(self):
        if self:
            print('777')

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # And finally, other business methods.
    # ------------------------------------------------------------------------------------------------------------------