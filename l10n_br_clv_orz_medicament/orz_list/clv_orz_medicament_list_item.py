# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class ORZMedicamentListItem(models.Model):
    _name = 'clv_orz_medicament.list.item'

    list_id = fields.Many2one('clv_orz_medicament.list', string='ORZ List',
                              help='ORZ List', required=False)
    medicament_id = fields.Many2one('clv_orz_medicament', string='Medicament',
                                    help='ORZ Medicament', required=False)
    notes = fields.Text(string='Notes')
    order = fields.Integer(string='Order',
                           default=10)

    # pf_0 = fields.Float(string='PF 0%')
    # pf_12 = fields.Float(string='PF 12%')
    # pf_17 = fields.Float(string='PF 17%')
    # pf_18 = fields.Float(string='PF 18%')
    # pf_19 = fields.Float(string='PF 19%')
    # pf_17_zfm = fields.Float(string='PF 17% ZONA FRANCA DE MANAUS')
    # pmc_0 = fields.Float(string='PMC 0%')
    # pmc_12 = fields.Float(string='PMC 12%')
    # pmc_17 = fields.Float(string='PMC 17%')
    # pmc_18 = fields.Float(string='PMC 18%')
    # pmc_19 = fields.Float(string='PMC 19%')
    # pmc_17_zfm = fields.Float(string='PMC 17% ZONA FRANCA DE MANAUS')
    ultima_alteracao = fields.Char(size=256, string='ULTIMA ALTERACAO')

    active = fields.Boolean('Active',
                            help='The active field allows you to hide the list item without removing it.',
                            default=1)

    _order = 'order'


class ORZMedicamentList(models.Model):
    _inherit = 'clv_orz_medicament.list'

    orz_list_item_ids = fields.One2many('clv_orz_medicament.list.item',
                                        'list_id',
                                        'ORZ List Itens')
