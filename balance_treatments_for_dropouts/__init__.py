from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'balance_treatments_for_dropouts'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TREATMENTS = ['red', 'blue', 'green']


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.completions_by_treatment = {color: 0 for color in C.TREATMENTS}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    color = models.StringField()


# PAGES
class Intro(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session

        player.color = min(
            C.TREATMENTS, key=lambda color: session.completions_by_treatment[color],
        )


class Task(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        session.completions_by_treatment[player.color] += 1


page_sequence = [Intro, Task]
