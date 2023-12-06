from otree.api import *


doc = """
Audio alert (speak some text to get the participant's attention, after a wait page)
"""


class C(BaseConstants):
    NAME_IN_URL = 'audio_alert'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class MyPage(Page):
    pass


class GBAT(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, GBAT, Results]
