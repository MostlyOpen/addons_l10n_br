# -*- coding: utf-8 -*-
###############################################################################
#
# For copyright and license notices, see __openerp__.py file in root directory
#
###############################################################################

from openerp import models, fields


class CMEDMedicament(models.Model):
    _name = 'clv_cmed_medicament'
    _inherit = 'clv_medicament.model'

    # med_abc = fields.Char(size=9, string='MED_ABC')
    # med_ctr = fields.Char(size=1, string='MED_CTR')
    # med_lab = fields.Char(size=6, string='MED_LAB')
    # lab_nom = fields.Char(size=30, string='LAB_NOM')
    # med_des = fields.Char(size=45, string='MED_DES')
    # med_apr = fields.Char(size=45, string='MED_APR')
    # med_barra = fields.Char(size=13, string='MED_BARRA')
    # med_gene = fields.Char(size=3, string='MED_GENE')
    # med_negpos = fields.Char(size=1, string='MED_NEGPOS')
    # med_princi = fields.Char(size=130, string='MED_PRINCI')
