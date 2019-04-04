# -*- coding: utf-8 -*-
{
    'name': "Manufacturing Raw Material",

    'summary': """
        Manufacturing Raw Material""",

    'description': """
        Manufacturing Raw Material
    """,

    'author': "AthmanZiri",
    'website': "https://www.innovus.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
    ],
    'application': True,
    'installable': True,
    'sequence': 1,
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}