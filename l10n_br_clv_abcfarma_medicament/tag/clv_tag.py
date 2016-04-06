# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class Tag(models.Model):
    _inherit = 'clv_tag'

    medicament_ids = fields.Many2many(
        'clv_abcfarma_medicament',
        'clv_abcfarma_medicament_tag_rel',
        'tag_id',
        'medicament_id',
        'ABCFarma Medicaments'
        )


class ABCFarmaMedicament(models.Model):
    _inherit = 'clv_abcfarma_medicament'

    tag_ids = fields.Many2many(
        'clv_tag',
        'clv_abcfarma_medicament_tag_rel',
        'medicament_id',
        'tag_id',
        'Tags'
        )
