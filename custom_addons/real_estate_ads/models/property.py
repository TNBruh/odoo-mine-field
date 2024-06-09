# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Property(models.Model):
    _name = "real_estate_ads.property"

    name = fields.Char(string="Name", required=True)
    property_tag_ids = fields.Many2many('real_estate_ads.property_tag', string='Property Tags')
    status = fields.Selection([
        ('new', 'New'),
        ('received', 'Offer Received'),
        ('accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], string='Status')
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    property_type_id = fields.Many2one(
        'real_estate_ads.property_type', 
        string='Property Type'
    )
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Float(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(
        string="Garden", 
        compute='_compute_garden',
    )
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ],string="Garden Orientation", default='north')
    offer_ids = fields.One2many(
        'real_estate_ads.property_offer', 
        'property_id', 
        string='Offers'
    )
    sales_id = fields.Many2one('res.users', string='Salesman')
    buyer_id = fields.Many2one('res.partner', string='Buyer', domain=[
        ('is_company', '=', True)
    ])
    total_area = fields.Integer('Total Area', compute='_compute_total_area')
    phone = fields.Char('Phone Number', related='buyer_id.phone')


    @api.depends("garden_area")
    def _compute_garden(self):
        for record in self:
            if record.garden_area:
                if record.garden_area <= 0:
                    record.garden = False
                else:
                    record.garden = True
            else:
                record.garden = False
    
    @api.depends('living_area','garden_area')
    def _compute_total_area(self):
        for record in self:
            living_area = 0 if not record.living_area else record.living_area
            garden_area = 0 if not record.garden_area else record.garden_area
            record.total_area = living_area + garden_area


    # def check_offers(self):
    #     self.ensure_one()
    #     return {
    #         'type': "ir.actions.act_window",
    #         'name': 'action_server_check_offers',
    #         'domain': [
    #             ('property_id', '=', self.id)
    #         ],
    #         'view_mode': 'tree',
    #         'res_model': 'real_estate_ads.property_offer',
    #         'view_id': 'real_estate_ads_property_offer_view_tree',
    #     }

class PropertyType(models.Model):
    _name = "real_estate_ads.property_type"

    name = fields.Char('Name', required=True)
    property_ids = fields.One2many('real_estate_ads.property', 'property_type_id', string='Properties')


class PropertyTag(models.Model):
    _name = "real_estate_ads.property_tag"

    name = fields.Char('Name', required=True)
    property_ids = fields.Many2many('real_estate_ads.property', string='Properties')