from odoo import fields, models,api


class ProductOrder(models.Model):

    _name = "product.order"
    _description = "Electronic Product Order"
    _rec_name='order_product'


    order_date=fields.Date(string="Order date",required=True)
    customer_id=fields.Many2one('product.customer',string="Customer",required=True)   
    cart_id=fields.Many2one('product.cart',string='Cart',required=True)
    order_product=fields.Char()
    total_amount=fields.Float(string="Total Amount",compute='_compute_total_amount')

    order_lines=fields.One2many('product.order.line','order_id',string='Order lines')

    @api.depends('order_lines.price')
    def _compute_total_amount(self):
        for order in self:
            # order.total_amount=sum(line.total_amount for line in order.order_lines)
            order.total_amount=sum(order.order_lines.mapped('price'))


   
    

    
   


    
   