from otree.api import *


doc = """
Live volunteer's dilemma (first player to click moves everyone forward).
"""


class C(BaseConstants):
    NAME_IN_URL = 'live_volunteer'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    REWARD = cu(1000)
    VOLUNTEER_COST = cu(500)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_volunteer = models.BooleanField(initial=False)


class Player(BasePlayer):
    is_volunteer = models.BooleanField()
    volunteer_id = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return not group.has_volunteer

    @staticmethod
    def live_method(player: Player, data):
        group = player.group

        # print('data is', data)

        if group.has_volunteer:
            return
        if data.get('volunteer'):
            group.has_volunteer = True
            # mark all other players as non-volunteers
            for p in player.get_others_in_group():
                p.payoff = C.REWARD
                p.is_volunteer = False
            # mark myself as a volunteer
            player.is_volunteer = True
            player.payoff = C.REWARD - C.VOLUNTEER_COST
            # broadcast to the group that the game is finished.
            return {0: dict(finished=True)}

    @staticmethod
    def error_message(player: Player, values):
        """Prevent users from proceeding before someone has volunteered."""
        group = player.group
        if not group.has_volunteer:
            return "Can't move forward"


class Results(Page):
    pass


page_sequence = [MyPage, Results]
