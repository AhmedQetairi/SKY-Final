# -*- coding: utf-8 -*-
# from odoo import http


# class Sky-management(http.Controller):
#     @http.route('/sky-management/sky-management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sky-management/sky-management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sky-management.listing', {
#             'root': '/sky-management/sky-management',
#             'objects': http.request.env['sky-management.sky-management'].search([]),
#         })

#     @http.route('/sky-management/sky-management/objects/<model("sky-management.sky-management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sky-management.object', {
#             'object': obj
#         })
