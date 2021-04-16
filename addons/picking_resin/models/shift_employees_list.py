# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import api, fields, models, _


# 3 :  imports of odoo modules

# 4 :  imports from custom modules


_logger = logging.getLogger(__name__)


class ShiftEmployeesList(models.Model):
    """ 
    Список работников при регистрации смены с указанием типа работ и количества выолненого
    """ 

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'picking_resin.shift_employees_list'
    _description = 'Employees list of shift'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
    )

    type_of_employment = fields.Many2one(
        comodel_name='picking_resin.types_of_employment',
        related='name.type_of_employment',
        string='Type of employment',
    )
    """ Тип найма """

    quantity = fields.Float(
        string='Quantity',
        digits=(8,2),
    )

    department_id = fields.Many2one(
        comodel_name='hr.department',
        string='District',
    )

    shift_date = fields.Datetime(
        string='Shift Date',
    )

    key = fields.Char(
        string='Unique key record',
    )

    work_type_id = fields.Many2one(
        comodel_name='picking_resin.work_types',
        string='Work type'
    )

    work_uom = fields.Many2one(
        related='work_type_id.measure_unit',
        string='Work UoM'
    )

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