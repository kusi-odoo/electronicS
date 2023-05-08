from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta

class Product(models.Model):
    _name = "product"
    _description = "Product"
    _log_access = False

    name = fields.Char(required=True,string="Product Name")
    description=fields.Text(string='Description')
    price=fields.Float(string="Price",required=True)
    company_name=fields.Char()
    product_details=fields.Char()
    product_mfg=fields.Datetime()

    # carts=fields.Many2many('product.cart',string='Carts')
   

    state = fields.Selection(
            selection=[
                ("new", "New"),
                ("sold", "Sold"),
                ("canceled", "Canceled"),
            ],
            string="Status",
            required=True,
            copy=False,
            default="new",
        )


