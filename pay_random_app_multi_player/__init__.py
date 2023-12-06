from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pay_random_app1'
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
    pass


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        """
        In multiplayer games, payoffs are typically set in after_all_players_arrive,
        so that's what we demonstrate here.
        """
        import random

        for p in group.get_players():
            participant = p.participant
            potential_payoff = random.randint(100, 200)
            p.potential_payoff = potential_payoff
            # __name__ is a magic variable that contains the name of the current app
            participant.app_payoffs[__name__] = potential_payoff


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
