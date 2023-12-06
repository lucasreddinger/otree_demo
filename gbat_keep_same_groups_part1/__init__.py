from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'gbat_keep_same_groups'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class GBATWait(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        # save each participant's current group ID so it can be
        # accessed in the next app.
        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id


class MyPage(Page):
    pass


page_sequence = [GBATWait, MyPage]
