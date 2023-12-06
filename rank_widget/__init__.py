from otree.api import *


doc = """
"Widget to rank/reorder items". See http://sortablejs.github.io/Sortable/
for more examples.
"""


class C(BaseConstants):
    NAME_IN_URL = 'rank_widget'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = ['Martini', 'Margarita', 'White Russian', 'Pina Colada', 'Gin & Tonic']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.StringField()


class MyPage(Page):
    form_model = 'player'
    form_fields = ['ranking']


class Results(Page):
    pass


page_sequence = [MyPage, Results]
