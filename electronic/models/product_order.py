from odoo import fields, models,api


class ProductOrder(models.Model):

    _name = "product.order"
    _description = "Electronic Product Order"
    _rec_name='order_product'

    customer_id=fields.Many2one('product.customer',required=True)   
    order_product=fields.Char()
    order_date=fields.Datetime(default=fields.Datetime.now())
    cart_id=fields.Many2one('product.cart',string='Cart',required=True)
   
    

    
   


    
   