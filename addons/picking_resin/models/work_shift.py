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

    employee_ids = fields.Many2many(
        comodel_name='picking_resin.shift_employees_list',
        string='List employee',
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Selection method (methods used to return computed values for selection fields)
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    @api.onchange('name')
    def _onchange_department(self):
        if self.name:
            if not self.shift_date:
                self.shift_date = fields.Datetime.now()
            # scan-rescan employees
            item_env = self.env['picking_resin.shift_employees_list']
            key = str((self.name.id, self.shift_date))
            for records in self.employee_ids:
                for record in records:
                    item_env.search([
                        ('name', '=', record.name.id),
                        ('department_id', '=', record.department_id.id),
                        ('shift_date', '=', record.shift_date),
                        ('key', '=', key)
                    ]).unlink()
            teams = self.env['hr.employee'].search([
                ('department_id', '=', self.name.id),
            ])
            for record in teams:
                vals = {
                    'name': record.id,
                    'quantity': 0.0,
                    'department_id': self.name.id,
                    'shift_date': self.shift_date,
                    'key': key,
                }
                item_env.create(vals)
            self.employee_ids = item_env.search([
                ('department_id', '=', self.name.id),
                ('shift_date', '=', self.shift_date),
                ('key', '=', key)
            ])

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------

    @api.model
    def create(self,vals_list):
        res = super(WorkShift, self).create(vals_list)
        names = []
        for records in res.employee_ids:
            for record in records:
                names.append(record.name.id)
        item_env = self.env['picking_resin.shift_employees_list']
        key = str((res.name.id, res.shift_date))
        item_env.search([
            ('key', '=', key),
            ('name', 'not in', names)
        ]).unlink()
        return res

    def write(self, vals_list):
        res = super(WorkShift, self).write(vals_list)
        names = []
        for records in self.employee_ids:
            for record in records:
                names.append(record.name.id)
        item_env = self.env['picking_resin.shift_employees_list']
        key = str((self.name.id, self.shift_date))
        item_env.search([
            ('key', '=', key),
            ('name', 'not in', names)
        ]).unlink()
        return res

    def unlink(self):
        item_env = self.env['picking_resin.shift_employees_list']
        key = str((self.name.id, self.shift_date))
        item_env.search([
            ('key', '=', key),
        ]).unlink()
        res = super().unlink()
        return res

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # And finally, other business methods.
    # ------------------------------------------------------------------------------------------------------------------