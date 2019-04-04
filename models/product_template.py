# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OriginType(models.Model):
    _name = 'origin.type'
    _description = 'Origin Type'
    _rec_name = 'name'

    name = fields.Char('Origin Type')


class RawMaterialType(models.Model):
    _name = 'raw.material.type'
    _description = 'Raw Material Type'
    
    name = fields.Char('Raw material Type')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    origin_type = fields.Many2one('origin.type', string='Origin Type')
    grade = fields.Char('Grade')
    melt_flow = fields.Float('Melt Flow')
    density = fields.Float('Density')
    raw_material_type = fields.Many2one('raw.material.type', string='Material Type')
    slip = fields.Boolean('Slip')
    anti_block = fields.Boolean('Anti Block')
    is_raw_material = fields.Boolean('Is raw material')
    