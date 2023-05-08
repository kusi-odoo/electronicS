from odoo import fields, models, api


class ProductOrderLine(models.Model):

    _name = "product.order.line"
    _description = "Electronic Product Order Line"

    name = fields.Char(required=True)
    order_id = fields.Many2one('product.order', string='Order')
    product_id = fields.Many2one('product', string='Product')
    price = fields.Float(string='Price', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
