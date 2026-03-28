# -*- coding: utf-8 -*-
# from odoo import http


# class GsLashio(http.Controller):
#     @http.route('/gs_lashio/gs_lashio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gs_lashio/gs_lashio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gs_lashio.listing', {
#             'root': '/gs_lashio/gs_lashio',
#             'objects': http.request.env['gs_lashio.gs_lashio'].search([]),
#         })

#     @http.route('/gs_lashio/gs_lashio/objects/<model("gs_lashio.gs_lashio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gs_lashio.object', {
#             'object': obj
#         })

