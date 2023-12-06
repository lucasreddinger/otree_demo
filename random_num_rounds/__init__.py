from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'random_num_rounds'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 20


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random

    for p in subsession.get_players():
        p.participant.num_rounds = random.randint(1, 20)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_rounds = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        """
        Skip this page if the round number has exceeded the participant's designated
        number of rounds.
        """

        participant = player.participant

        return player.round_number < participant.num_rounds


class End(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [MyPage, End]
