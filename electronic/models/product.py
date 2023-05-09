from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError,ValidationError

class Product(models.Model):
    _name = "product"
    _description = "Product"
    _log_access = False

    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "The Price must be strictly positive"),
    ]

    name = fields.Char(required=True,string="Product Name")
    description=fields.Text(string='Description')
    price=fields.Float(string="Price",required=True)
    company_name=fields.Char()
    product_details=fields.Char()
    product_mfg=fields.Datetime()

    carts=fields.Many2many('product.cart',string='Carts')
   

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


     #------------------- Action Methods -------------------#
    


    def action_sold(self):
        for record in self:
            if record.state=='canceled':
                raise UserError("Canceled properties can't be sold.")
            record.state='sold'    


    def action_cancel(self):
        for record in self:
            if record.state=='sold':
                raise UserError("Sold properties can't be canceled")
            record.state='canceled'             


