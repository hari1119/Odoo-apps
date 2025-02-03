# -*- coding: utf-8 -*-
{
    'name': "Required Fields Indicator",

    'summary': "Indicate all required fields in odoo",

    'description': """
               Indicate all required fields in odoo standard like odoo previous version.
    """,
    'author': "Hari",
    'website': "https://hari1119.github.io/",
    'category': 'Extra Rights',
    'version': '17.0.0.0',
    'depends': ['base','web'],
    'installable': True,
    'images': ['static/description/banner.gif'],
    'assets': {
        'web.assets_backend': [
            'required_fields_indicator/static/scss/fields.scss',
        ],
    },
    'license': 'LGPL-3',
    'data': [],
    'demo': [],
}

