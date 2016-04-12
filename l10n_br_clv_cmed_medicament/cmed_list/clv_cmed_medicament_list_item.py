# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class CMEDMedicamentListItem(models.Model):
    _name = 'clv_cmed_medicament.list.item'

    list_id = fields.Many2one('clv_cmed_medicament.list', string='CMED List',
                              help='CMED List', required=False)
    medicament_id = fields.Many2one('clv_cmed_medicament', string='Medicament',
                                    help='CMED Medicament', required=False)
    notes = fields.Text(string='Notes')
    order = fields.Integer(string='Order',
                           default=10)
    # pmc = fields.Float(string='PMC [R$]')
    # desconto = fields.Float(string='Desconto [%]')
    # preco_venda = fields.Float(string='Preço Venda [%]')

    # med_uni = fields.Float(string='MED_UNI')
    # med_ipi = fields.Float(string='MED_IPI')
    # med_dtvig = fields.Date('MED_DTVIG')
    # exp_13 = fields.Boolean('EXP_13')
    # med_regims = fields.Char(size=13, string='MED_REGIMS')
    # med_varpre = fields.Char(size=1, string='MED_VARPRE')

    # med_pco18 = fields.Float(string='MED_PCO18')
    # med_pla18 = fields.Float(string='MED_PLA18')
    # med_fra18 = fields.Float(string='MED_FRA18')
    # med_pco17 = fields.Float(string='MED_PCO17')
    # med_pla17 = fields.Float(string='MED_PLA17')
    # med_fra17 = fields.Float(string='MED_FRA17')
    # med_pco12 = fields.Float(string='MED_PCO12')
    # med_pla12 = fields.Float(string='MED_PLA12')
    # med_fra12 = fields.Float(string='MED_FRA12')
    # med_pco19 = fields.Float(string='MED_PCO19')
    # med_pla19 = fields.Float(string='MED_PLA19')
    # med_fra19 = fields.Float(string='MED_FRA19')
    # med_pcozfm = fields.Float(string='MED_PCOZFM')
    # med_plazfm = fields.Float(string='MED_PLAZFM')
    # med_frazfm = fields.Float(string='MED_FRAZFM')
    # med_pco0 = fields.Float(string='MED_PCO0')
    # med_pla0 = fields.Float(string='MED_PLA0')
    # med_fra0 = fields.Float(string='MED_FRA0')
    # # included = fields.Boolean('Included')
    active = fields.Boolean('Active',
                            help='The active field allows you to hide the list item without removing it.',
                            default=1)

    _order = 'order'


class CMEDMedicamentList(models.Model):
    _inherit = 'clv_cmed_medicament.list'

    cmed_list_item_ids = fields.One2many('clv_cmed_medicament.list.item',
                                         'list_id',
                                         'CMED List Itens')
