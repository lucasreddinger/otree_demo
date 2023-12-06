from otree.api import *


doc = """
Preserve same groups as a previous app that used group_by_arrival time.
"""


class C(BaseConstants):
    NAME_IN_URL = 'gbat_keep_same_groups_part2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    # we now place users into different baskets, according to their group in the previous app.
    # the dict 'd' will contain all these baskets.
    d = {}
    for p in waiting_players:
        group_id = p.participant.past_group_id
        if group_id not in d:
            # since 'd' is initially empty, we need to initialize an empty list (basket)
            # each time we see a new group ID.
            d[group_id] = []
        players_in_my_group = d[group_id]
        players_in_my_group.append(p)
        if len(players_in_my_group) == 2:
            return players_in_my_group
        # print('d is', d)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class GBATWait(WaitPage):
    group_by_arrival_time = True


class MyPage(Page):
    pass


page_sequence = [GBATWait, MyPage]
