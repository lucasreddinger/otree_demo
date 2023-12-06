from otree.api import *

doc = """
Back button for multiple instructions pages
"""

class C(BaseConstants):
    NAME_IN_URL = 'back_button'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Instructions(Page):
    pass


class Task(Page):
    pass


page_sequence = [Instructions, Task]
