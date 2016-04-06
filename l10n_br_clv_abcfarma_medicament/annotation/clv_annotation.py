# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class ABCFarmaMedicament(models.Model):
    _inherit = 'clv_abcfarma_medicament'

    annotation_ids = fields.Many2many(
        'clv_annotation',
        'clv_abcfarma_medicament_annotation_rel',
        'medicament_id',
        'annotation_id',
        'Annotations'
        )


class Annotation(models.Model):
    _inherit = 'clv_annotation'

    medicament_ids = fields.Many2many(
        'clv_abcfarma_medicament',
        'clv_abcfarma_medicament_annotation_rel',
        'annotation_id',
        'medicament_id',
        'ABCFarma Medicaments'
        )
