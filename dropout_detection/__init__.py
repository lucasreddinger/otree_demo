from otree.api import *


doc = """
Dropout detection (if user does not submit page in time)
"""


class C(BaseConstants):
    NAME_IN_URL = 'detect_dropout'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_dropout = models.BooleanField(initial=False)


class Page1(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # note: bugfix
        if timeout_happened:
            player.is_dropout = True


class ByeDropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.is_dropout

    @staticmethod
    def error_message(player: Player, values):
        return "Cannot proceed past this page"


class Page2(Page):
    pass


page_sequence = [Page1, ByeDropout, Page2]
