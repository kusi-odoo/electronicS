from odoo import fields, models,api


class ProductCartLine(models.Model):

    _name = "product.cart.line"
    _description = "Electronic Product Cart Line"
    _rec_name="cart_id"

    product_id=fields.Many2one('product',string='Product',required=True)
    cart_id=fields.Many2one('product.cart',string='Cart',required=True)
    quantity=fields.Integer('Quantity',required=True,default=1)
    price=fields.Float('Price',compute='_compute_price')


    @api.depends('product_id','quantity')
    def _compute_price(self):
        for line in self:
            line.price=line.product_id.price*line.quantity

    


   
    
   