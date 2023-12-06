from otree.api import *


doc = """
All you need is a participant field called 'progress' then keep adding 1 to it.
"""


class C(BaseConstants):
    NAME_IN_URL = 'progress_bar'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        participant = player.participant
        participant.progress = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Page1(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        # remember to add 'progress' to PARTICIPANT_FIELDS.
        participant.progress += 1


class Page2(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        # progress can be defined in different ways, not only by page number
        # (especially if pages get skipped)
        # so feel free to do things like:
        # - incrementing by more than 1:
        # participant.progress += 2
        # - setting to a specific valueInput:
        # participant.progress = 8
        participant.progress += 1


page_sequence = [Page1, Page2]
