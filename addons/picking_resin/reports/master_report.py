# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import api, fields, models, _
from odoo import tools

# 3 :  imports of odoo modules

# 4 :  imports from custom modules


_logger = logging.getLogger(__name__)


class MasterReport(models.Model):
    """
    Отчет по работам для мастера
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _auto = False

    _name = 'picking_resin.master_report'
    _description = 'Master Report'

    _table = 'picking_resin_master_report'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
    )

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

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Selection method (methods used to return computed values for selection fields)
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'picking_resin_master_report')
        self.env.cr.execute(
            u"""
            CREATE OR REPLACE VIEW picking_resin_master_report AS (
            SELECT
                emp_lst.id as id,
                emp_lst.name as name,
                emp_lst.quantity as quantity,
                emp_lst.department_id as department_id,
                emp_lst.shift_date as shift_date,
                emp_lst.work_type_id as work_type_id
            FROM picking_resin_shift_employees_list as emp_lst
            WHERE emp_lst.key IN (
                SELECT shift_key
                FROM picking_resin_work_shift
            )
            )
            """.format()
        )

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # And finally, other business methods.
    # ------------------------------------------------------------------------------------------------------------------'
