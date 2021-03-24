# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import api, fields, models, _


# 3 :  imports of odoo modules

# 4 :  imports from custom modules


_logger = logging.getLogger(__name__)


class HrEmployeeExt(models.Model):
    """
    Расширение модели Сотрудники
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'hr.employee'

    _inherit = [
        'hr.employee',
        'mail.thread',
    ]
    _description = ''

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    user_id = fields.Many2one(
        comodel_name='res.users',
        track_visibility=True,  # переопределен для добавления трекинга
    )
    """ Аккаунт пользователя """

    parent_id = fields.Many2one(
        comodel_name='hr.employee',
        track_visibility=True,  # переопределен для добавления трекинга
    )
    """ Мастер сотрудника """

    department_id = fields.Many2one(
        comodel_name='hr.department',
        track_visibility=True,  # переопределен для добавления трекинга
    )
    """ Департамент сотрудника (участок) """

    type_of_employment = fields.Char(
        string='Type of employment',
    )
    """ Тип найма """

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