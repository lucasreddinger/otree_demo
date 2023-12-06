from otree.api import *


doc = """Practice rounds"""


class C(BaseConstants):
    NAME_IN_URL = 'practice_rounds'
    PLAYERS_PER_GROUP = None
    NUM_PRACTICE_ROUNDS = 2
    NUM_REAL_ROUNDS = 10
    NUM_ROUNDS = NUM_PRACTICE_ROUNDS + NUM_REAL_ROUNDS


class Subsession(BaseSubsession):
    is_practice_round = models.BooleanField()
    real_round_number = models.IntegerField()


def creating_session(subsession: Subsession):
    # In Python, 'a <= b' produces either True or False.
    subsession.is_practice_round = (
        subsession.round_number <= C.NUM_PRACTICE_ROUNDS
    )
    if not subsession.is_practice_round:
        subsession.real_round_number = (
            subsession.round_number - C.NUM_PRACTICE_ROUNDS
        )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.IntegerField()
    solution = models.IntegerField()
    is_correct = models.BooleanField()


class Play(Page):
    form_model = 'player'
    form_fields = ['response']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # the **2 is just an example used in this game (squaring a number)
        player.solution = player.round_number ** 2

        player.is_correct = player.response == player.solution


class PracticeFeedback(Page):
    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.is_practice_round


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        score = 0
        for p in player.in_rounds(
            C.NUM_PRACTICE_ROUNDS + 1, C.NUM_ROUNDS
        ):
            score += p.is_correct
        return dict(score=score)


page_sequence = [Play, PracticeFeedback, Results]
