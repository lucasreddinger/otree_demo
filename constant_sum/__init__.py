from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'constant_sum'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    a = models.CurrencyField()
    b = models.CurrencyField()
    c = models.CurrencyField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['a', 'b', 'c']

    @staticmethod
    def error_message(player: Player, values):
        # since 'values' is a dict, you could also do sum(values.values())
        if values['a'] + values['b'] + values['c'] != 100:
            return 'Numbers must add up to 100'


page_sequence = [MyPage]
