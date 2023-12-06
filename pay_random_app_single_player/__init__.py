from otree.api import *


doc = """
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_app2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        # initialize an empty dict to store how much they made in each app
        p.participant.app_payoffs = {}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    potential_payoff = models.CurrencyField()


# PAGES
class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        """in a single-player game you typically set payoff in before_next_page,
        so that's what we demonstrate here.
        """
        participant = player.participant
        import random

        potential_payoff = random.randint(100, 200)
        player.potential_payoff = potential_payoff
        # this is designed for apps that have a single round.
        # if your app has multiple rounds, see the pay_random_round app.
        participant.app_payoffs[__name__] = potential_payoff


class Results(Page):
    pass


page_sequence = [MyPage, Results]
