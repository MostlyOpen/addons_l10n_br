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

    principio_ativo = fields.Char(size=128, string='Principio Ativo')
    cnpj = fields.Char(size=128, string='CNPJ')
    latoratorio = fields.Char(size=128, string='Laboratorio')
    codigo_ggrem = fields.Char(size=15, string='Codigo GGREM (2)')
    registro = fields.Char(size=13, string='Registro')
    ean = fields.Char(size=13, string='EAN')
    produto = fields.Char(size=128, string='Produto')
    apresentacao = fields.Char(size=128, string='Apresentacao')
    classe_terapeutica = fields.Char(size=128, string='Classe Terapeutica')

    restr_hospitalar = fields.Char(size=256, string='RESTRICAO_HOSPITALAR')
    cap = fields.Char(size=256, string='CAP')
    confaz_87 = fields.Char(size=256, string='CONFAZ_87')
    analise_recursal = fields.Char(size=256, string='ANALISE_RECURSAL')
