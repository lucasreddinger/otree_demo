from otree.api import *


doc = """
Slider with live updating label
"""


class C(BaseConstants):
    NAME_IN_URL = 'slider_live_label'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    give = models.IntegerField(
        min=0, max=C.ENDOWMENT, label="How much do you want to give?"
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['give']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)


page_sequence = [MyPage]
