# -*- coding: utf-8 -*-
from odoo import http

# class BalanceSheetGenerator(http.Controller):
#     @http.route('/balance_sheet_generator/balance_sheet_generator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/balance_sheet_generator/balance_sheet_generator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('balance_sheet_generator.listing', {
#             'root': '/balance_sheet_generator/balance_sheet_generator',
#             'objects': http.request.env['balance_sheet_generator.balance_sheet_generator'].search([]),
#         })

#     @http.route('/balance_sheet_generator/balance_sheet_generator/objects/<model("balance_sheet_generator.balance_sheet_generator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('balance_sheet_generator.object', {
#             'object': obj
#         })