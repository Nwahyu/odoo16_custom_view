from odoo import _, api, fields, models

class nama_satu(models.Model):
    _name = 'nama.satu'
    _description = 'nama.satu'
    _rec_name = 'nama'
    
    nama = fields.Char('nama')
    nomor = fields.Integer('nomor')
    betulan = fields.Boolean('betulan')