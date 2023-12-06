from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'gbat_fallback_solo_task_part0'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        import time

        participant.wait_page_arrival = time.time()


page_sequence = [MyPage]
