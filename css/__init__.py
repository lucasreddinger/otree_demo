from otree.api import *


doc = """
Using CSS to style timer and chat box.
"""


class C(BaseConstants):
    NAME_IN_URL = 'css'
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
    timeout_seconds = 30 * 60


page_sequence = [MyPage]
