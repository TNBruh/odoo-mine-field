from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name = "real_estate_ads.property_offer"

    price = fields.Float('Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status')
    partner_id = fields.Many2one('res.partner', string='Customer')
    property_id = fields.Many2one('real_estate_ads.property', string='Property')
    validity = fields.Integer('Validity')
    deadline = fields.Date('Deadline', compute='_compute_deadline') #, inverse='_inverse_deadline'
    creation_date = fields.Date('Creation Date', default=fields.Date.today())

    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for record in self:
            if record.creation_date and record.validity:
                record.deadline = record.creation_date + timedelta(days=record.validity)
            else:
                record.deadline = False

    @api.constrains('validity')
    def _constrain_validity(self):
        for record in self:
            if not record.validity:
                raise ValidationError("Empty validity")
            elif record.validity <= 0:
                raise ValidationError("validity <= 0")

    def _inverse_deadline(self):
        for record in self:
            if record.deadline and record.creation_date:
                record.validity = (record.deadline - record.creation_date).days
            else:
                record.validity = False