# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class CMEDMedicamentList(models.Model):
    _name = 'clv_cmed_medicament.list'

    name = fields.Char('CMED List', required=True, size=64)
    code = fields.Char('CMED List Code', size=128, required=False)
    description = fields.Char(string='Description', size=256)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active',
                            help='The active field allows you to hide the list without removing it.',
                            default=1)

    _sql_constraints = [
        ('uniq_list_name', 'unique(name)', "Error! The List Name must be unique!"),
        ('uniq_list_code', 'unique(code)', "Error! The List Code must be unique!"),
        ]
