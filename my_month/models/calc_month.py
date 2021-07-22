from odoo import models, fields


class CalcMonth(models.Model):
    _name = 'calc.month'
    my_selection_field = fields.Selection(
        [
            ('option1', 'Styczen'),
            ('option2', 'Luty'),
            ('option3', 'Marzec'),
            ('option4', 'Kwiecień'),
            ('option5', 'Maj'),
            ('option6', 'Czerwiec'),
            ('option7', 'Lipiec'),
            ('option8', 'Sierpien'),
            ('option9', 'Wrzesien'),
            ('option10', 'Pazdziernik'),
            ('option11', 'Listopad'),
            ('option12', 'Grudzien'),
        ], string='My Selection Field'
    )
    my_days = fields.Integer(String="Days")

