from otree.api import *

doc = """group_by_arrival_time timeout (continue with solo task)"""


class C(BaseConstants):
    NAME_IN_URL = 'gbat_fallback_solo_task_part1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def group_by_arrival_time_method(subsession, waiting_players):
    print('waiting_players', waiting_players)
    if len(waiting_players) >= 2:
        return waiting_players[:2]
    for player in waiting_players:
        if waiting_too_long(player):
            # make a single-player group.
            print('waiting too long, making 1 player group')
            return [player]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    favorite_color = models.StringField()


def waiting_too_long(player: Player):
    participant = player.participant

    import time

    # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return time.time() - participant.wait_page_arrival > 60


class GBAT(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        # if it's a solo group (1 player), skip this app
        # and go to the next app (which in this case is a
        # single-player task)
        if len(player.get_others_in_group()) == 0:
            return upcoming_apps[0]


class GroupTask(Page):
    form_model = 'player'
    form_fields = ['favorite_color']


class MyWait(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [GBAT, GroupTask, MyWait, Results]
