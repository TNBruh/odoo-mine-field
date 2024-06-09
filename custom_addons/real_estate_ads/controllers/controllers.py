# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateAds(http.Controller):
#     @http.route('/real_estate_ads/real_estate_ads', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_ads/real_estate_ads/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_ads.listing', {
#             'root': '/real_estate_ads/real_estate_ads',
#             'objects': http.request.env['real_estate_ads.real_estate_ads'].search([]),
#         })

#     @http.route('/real_estate_ads/real_estate_ads/objects/<model("real_estate_ads.real_estate_ads"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_ads.object', {
#             'object': obj
#         })

