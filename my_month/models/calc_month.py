from odoo import models, fields, api


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
        ], string='My Selection Field',
    )
    my_days = fields.Integer(String="Days")

    @api.onchange('my_selection_field')
    def calc_month(self):
        print("======================================")
        print("vartosc w month: ", self.my_selection_field)

        self.my_days = self.check_month_value(self.my_selection_field)
        print(self.my_days)

    @staticmethod
    def check_month_value(par):
        switcher = {
            'option1': 31,
            'option2': 28,
            'option3': 31,
            'option4': 30,
            'option5': 31,
            'option6': 30,
            'option7': 31,
            'option8': 31,
            'option9': 30,
            'option10': 31,
            'option11': 30,
            'option12': 31,
        }
        return switcher.get(par, 'Invalid month of year')





