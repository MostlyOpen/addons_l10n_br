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

from openerp import models, fields, api


class ABCFarmaMedicament(models.Model):
    _name = 'clv_abcfarma_medicament'
    _inherit = 'clv_medicament.model'

    name = fields.Char(string="Product Name", select=True, required=True, store=True,
                       compute="_get_compute_name",
                       help='Use "/" to get an automatic new Product Name.')

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

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            # if record['code']:
            #     name = name + ' {' + record['code'] + '}'
            res.append((record['id'], name))
        return res

    @api.depends('med_abc', 'med_des', 'med_princi', 'med_apr', 'lab_nom', 'med_barra')
    def _get_compute_name(self):
        if not self.name:
            med_abc = ''
            if self.med_abc:
                med_abc = self.med_abc
            med_des = ''
            if self.med_des:
                med_des = self.med_des
            med_princi = ''
            if self.med_princi:
                med_princi = self.med_princi
            med_apr = ''
            if self.med_apr:
                med_apr = self.med_apr
            lab_nom = ''
            if self.lab_nom:
                lab_nom = self.lab_nom
            med_barra = ''
            if self.med_barra:
                med_barra = self.med_barra
            self.name = '[' + med_abc + '] ' + \
                        med_des + \
                        ' (' + med_princi + ') ' + \
                        med_apr + ' - ' + \
                        lab_nom + \
                        ' [' + med_barra + '] '
            # self.name = '' + med_des + \
            #             ' (' + med_princi + ') ' + \
            #             med_apr + ' - ' + \
            #             lab_nom + \
            #             ' [' + med_barra + '] '

    @api.onchange('name')
    def onchange_name(self):
        if self.name == '/':
            med_abc = ''
            if self.med_abc:
                med_abc = self.med_abc
            med_des = ''
            if self.med_des:
                med_des = self.med_des
            med_princi = ''
            if self.med_princi:
                med_princi = self.med_princi
            med_apr = ''
            if self.med_apr:
                med_apr = self.med_apr
            lab_nom = ''
            if self.lab_nom:
                lab_nom = self.lab_nom
            med_barra = ''
            if self.med_barra:
                med_barra = self.med_barra
            self.name = '[' + med_abc + '] ' + \
                        med_des + \
                        ' (' + med_princi + ') ' + \
                        med_apr + ' - ' + \
                        lab_nom + \
                        ' [' + med_barra + '] '
            # self.name = '' + med_des + \
            #             ' (' + med_princi + ') ' + \
            #             med_apr + ' - ' + \
            #             lab_nom + \
            #             ' [' + med_barra + '] '
