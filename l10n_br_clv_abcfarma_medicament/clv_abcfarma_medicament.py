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
    med_barra = fields.Char(size=13, string='MED_BARRA')
    med_gene = fields.Char(size=3, string='MED_GENE')
    med_negpos = fields.Char(size=1, string='MED_NEGPOS')
    med_princi = fields.Char(size=130, string='MED_PRINCI')
