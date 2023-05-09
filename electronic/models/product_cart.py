from odoo import fields, models


class ProductCart(models.Model):

    _name = "product.cart"
    _description = "Electronic Product Cart"
    _rec_name='cust_id'


   
    cust_id=fields.Many2one('product.customer',string="Customer",required=True)
    total_amount=fields.Float(string='Tolat Amount',compute='_compute_total_amount')

    cart_items=fields.One2many('product.cart.line','cart_id',string='Cart Item')



    def _compute_total_amount(self):
        for cart in self:
            cart.total_amount=sum(item.price*item.quantity for item in cart.cart_items)
   