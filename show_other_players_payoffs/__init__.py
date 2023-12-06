from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'show_other_players_payoffs'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(others=player.get_others_in_group())


page_sequence = [Results]
