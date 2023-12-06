from otree.api import *

doc = """History table"""


class C(BaseConstants):
    NAME_IN_URL = 'history_table'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField(label="Enter a number")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['number']


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(me_in_all_rounds=player.in_all_rounds())


page_sequence = [MyPage, Results]
