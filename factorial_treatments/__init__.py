from otree.api import *

doc = """Randomize multiple factors in a balanced way"""


class C(BaseConstants):
    NAME_IN_URL = 'randomize_cross_product'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools

    treatments = itertools.cycle(
        itertools.product([True, False], [True, False], [100, 200, 300])
    )
    for p in subsession.get_players():
        treatment = next(treatments)
        # print('treatment is', treatment)
        p.time_pressure = treatment[0]
        p.high_tax = treatment[1]
        p.endowment = treatment[2]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_pressure = models.BooleanField()
    high_tax = models.BooleanField()
    endowment = models.CurrencyField()


class MyPage(Page):
    pass


page_sequence = [MyPage]
