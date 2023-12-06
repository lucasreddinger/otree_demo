from otree.api import *


doc = """
Sliders and checkboxes that don't get wiped out on form reload.
Also works for text/number inputs, etc. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'persist_raw'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    f_int = models.IntegerField(min=10)
    f_bool1 = models.BooleanField(blank=True)
    f_bool2 = models.BooleanField(blank=True)
    f_bool3 = models.BooleanField(blank=True)
    f_bool4 = models.BooleanField(blank=True)
    f_bool5 = models.BooleanField(blank=True)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = [
        'f_int',
        'f_bool1',
        'f_bool2',
        'f_bool3',
        'f_bool4',
        'f_bool5',
    ]


page_sequence = [MyPage]
