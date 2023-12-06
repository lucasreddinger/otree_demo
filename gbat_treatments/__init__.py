from otree.api import *


doc = """
Conventionally, group-level treatments are assigned in creating_session:

for g in subsession.get_groups():
    g.treatment = random.choice([True, False])

However, this doesn't work when using group_by_arrival_time,
because groups are not determined until players arrive at the wait page.
(All players are in the same group initially.)
Instead, you need to assign treatments in after_all_players_arrive.
"""


class C(BaseConstants):
    NAME_IN_URL = 'gbat_treatments'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    treatment = models.BooleanField()


class Player(BasePlayer):
    pass


class GBATWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        import random

        group.treatment = random.choice([True, False])


class MyPage(Page):
    pass


page_sequence = [GBATWaitPage, MyPage]
