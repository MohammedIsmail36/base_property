# -*- coding: utf-8 -*-
{
    'name': "property",
    'summary': """ Managing all real estate """,
    'description': """  Managing all real estate through an integrated system and linking it to accounts and all other branches""",
    'author': "Mohamed Ahmed Ismail",
    'website': "http://www.mohamedismail.net",
    'category': 'Real Estate',
    'version': '15.0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'account'],
    # always loaded
    'data': [
        # Security Files
        'security/ir.model.access.csv',
        # Data Files
        # wizard Files
        # Views Files
        'views/views.xml',
        'views/main_property_view.xml',
        'views/sub_property_view.xml',
        'views/property_type_view.xml',
        'views/account_move_view.xml',
        #Report
        'report/main_property_details_report_template.xml',
        'report/main_property_details_report_template_a.xml',
        'report/main_property_details_report_template_b.xml',
        'report/main_property_details_report_template_c.xml',
        # report actions
        'report/report_actions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
