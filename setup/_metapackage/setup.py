import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-stock-logistics-reporting",
    description="Meta package for oca-stock-logistics-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-delivery_line_sale_line_position',
        'odoo14-addon-stock_card_report',
        'odoo14-addon-stock_picking_group_by_partner_by_carrier_sale_line_position',
        'odoo14-addon-stock_picking_report_valued',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
