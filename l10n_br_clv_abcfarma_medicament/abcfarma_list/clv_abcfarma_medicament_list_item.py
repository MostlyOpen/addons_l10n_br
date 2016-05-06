# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields


class ABCFarmaMedicamentListItem(models.Model):
    _name = 'clv_abcfarma_medicament.list.item'

    list_id = fields.Many2one('clv_abcfarma_medicament.list', string='ABCFarma List',
                              help='ABCFarma List', required=False)
    medicament_id = fields.Many2one('clv_abcfarma_medicament', string='Medicament',
                                    help='ABCFarma Medicament', required=False)
    notes = fields.Text(string='Notes')
    order = fields.Integer(string='Order',
                           default=10)

    med_uni = fields.Float(string='MED_UNI')
    med_ipi = fields.Float(string='MED_IPI')
    med_dtvig = fields.Date('MED_DTVIG')
    exp_13 = fields.Boolean('EXP_13')
    med_regims = fields.Char(size=13, string='MED_REGIMS')
    med_varpre = fields.Char(size=1, string='MED_VARPRE')

    med_pco18 = fields.Float(string='MED_PCO18')
    med_pla18 = fields.Float(string='MED_PLA18')
    med_fra18 = fields.Float(string='MED_FRA18')
    med_pco17 = fields.Float(string='MED_PCO17')
    med_pla17 = fields.Float(string='MED_PLA17')
    med_fra17 = fields.Float(string='MED_FRA17')
    med_pco12 = fields.Float(string='MED_PCO12')
    med_pla12 = fields.Float(string='MED_PLA12')
    med_fra12 = fields.Float(string='MED_FRA12')
    med_pco19 = fields.Float(string='MED_PCO19')
    med_pla19 = fields.Float(string='MED_PLA19')
    med_fra19 = fields.Float(string='MED_FRA19')
    med_pcozfm = fields.Float(string='MED_PCOZFM')
    med_plazfm = fields.Float(string='MED_PLAZFM')
    med_frazfm = fields.Float(string='MED_FRAZFM')
    med_pco0 = fields.Float(string='MED_PCO0')
    med_pla0 = fields.Float(string='MED_PLA0')
    med_fra0 = fields.Float(string='MED_FRA0')
    active = fields.Boolean('Active',
                            help='The active field allows you to hide the list item without removing it.',
                            default=1)

    _order = 'order'


class ABCFarmaMedicamentList(models.Model):
    _inherit = 'clv_abcfarma_medicament.list'

    abcfarma_list_item_ids = fields.One2many('clv_abcfarma_medicament.list.item',
                                             'list_id',
                                             'ABCFarma List Itens')
