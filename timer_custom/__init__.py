from otree.api import *


doc = """
Timer: replacing the default timer with your own
"""


class C(BaseConstants):
    NAME_IN_URL = 'timer_custom'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    timeout_seconds = 60


page_sequence = [MyPage]
