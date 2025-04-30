{
    "name": "Sales, Purchase & Delivery Customization",
    "version": "18.0.0.1",
    "category": "Custom",
    "description": """
        Pranav Parmar
    """,
    "website": "",
    "author": "Pranav Parmar",
    "license": "LGPL-3",
    "installable": True,
    "application": False,
    "summary": "",
    "depends": ["sale_management", "sale_purchase_stock", "mrp", "base_automation"],
    "data": [
        "data/automated_action.xml",
        "views/stock_picking_views.xml",
        "views/sale_order_views.xml",
        "views/res_partner_views.xml",
        "views/mrp_production_views.xml",
    ],
}
