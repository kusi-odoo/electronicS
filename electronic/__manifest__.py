{
    'name': "Electronic Shop",
    'version': '1.0',
    'depends': ['base'],
    'author': "Kuldeep Singh",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/product_cart_views.xml',
        'views/product_views.xml',
        'views/product_order_views.xml',
        'views/product_order_line_views.xml',
        'views/product_customer_views.xml',
        'views/electronic_shop_menus_views.xml',
       
         
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
 
    ],
    'application':True,
    'instalation':True,
}