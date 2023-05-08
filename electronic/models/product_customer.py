from odoo import fields, models,api


class ProductCustomer(models.Model):

    _name = "product.customer"
    _description = "Electronic Product Customer"
   
    name = fields.Char(required=True)
    email = fields.Char(required=True)
    phone = fields.Char()
    address = fields.Char()
   
   