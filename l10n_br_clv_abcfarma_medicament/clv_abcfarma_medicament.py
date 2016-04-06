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


class ABCFarmaMedicament(models.Model):
    _name = 'clv_abcfarma_medicament'
    _inherit = 'clv_medicament.model'

    med_abc = fields.Char(size=9, string='MED_ABC')
    med_ctr = fields.Char(size=1, string='MED_CTR')
    med_lab = fields.Char(size=6, string='MED_LAB')
    lab_nom = fields.Char(size=30, string='LAB_NOM')
    med_des = fields.Char(size=45, string='MED_DES')
    med_apr = fields.Char(size=45, string='MED_APR')
    # med_pco18 = fields.Float(string='MED_PCO18')
    # med_pla18 = fields.Float(string='MED_PLA18')
    # med_fra18 = fields.Float(string='MED_FRA18')
    # med_pco17 = fields.Float(string='MED_PCO17')
    # med_pla17 = fields.Float(string='MED_PLA17')
    # med_fra17 = fields.Float(string='MED_FRA17')
    # med_pco12 = fields.Float(string='MED_PCO12')
    # med_pla12 = fields.Float(string='MED_PLA12')
    # med_fra12 = fields.Float(string='MED_FRA12')
    # med_uni = fields.Float(string='MED_UNI')
    # med_ipi = fields.Float(string='MED_IPI')
    # med_dtvig = fields.date('MED_DTVIG')
    # exp_13 = fields.Boolean('EXP_13')
    med_barra = fields.Char(size=13, string='MED_BARRA')
    med_gene = fields.Char(size=3, string='MED_GENE')
    med_negpos = fields.Char(size=1, string='MED_NEGPOS')
    med_princi = fields.Char(size=130, string='MED_PRINCI')
    # med_pco19 = fields.Float(string='MED_PCO19')
    # med_pla19 = fields.Float(string='MED_PLA19')
    # med_fra19 = fields.Float(string='MED_FRA19')
    # med_pcozfm = fields.Float(string='MED_PCOZFM')
    # med_plazfm = fields.Float(string='MED_PLAZFM')
    # med_frazfm = fields.Float(string='MED_FRAZFM')
    # med_pco0 = fields.Float(string='MED_PCO0')
    # med_pla0 = fields.Float(string='MED_PLA0')
    # med_fra0 = fields.Float(string='MED_FRA0')
    # med_regims = fields.Char(size=13, string='MED_REGIMS')
    # med_varpre = fields.Char(size=1, string='MED_VARPRE')
