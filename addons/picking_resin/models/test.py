from odoo import fields, models, api


class TestModel(models.Model):
    _name = 'picking_resin.test_model2'
    _description = 'Simple test security'

    name = fields.Char()
