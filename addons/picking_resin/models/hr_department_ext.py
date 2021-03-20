# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences,PyProtectedMember
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)


class HrDepartmentExt(models.Model):
    """
    Расширение модели hr.department для Сбора Живицы
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _inherit = 'hr.department'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    active = fields.Boolean(
        track_visibility=True,
    )
    """ Признак софт-удаления записи """

    # Selection method (methods used to return computed values for selection fields)
    # ------------------------------------------------------------------------------------------------------------------

    # Compute and search fields, in the same order of fields declaration
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
