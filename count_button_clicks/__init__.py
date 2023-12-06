from otree.api import *

doc = """Count button clicks"""


class C(BaseConstants):
    NAME_IN_URL = 'count_button_clicks'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    button_clicks = models.IntegerField(initial=0)
    link_clicks = models.IntegerField(initial=0)


# PAGES
class MyPage(Page):
    @staticmethod
    def live_method(player: Player, data):
        if data == 'clicked-button':
            player.button_clicks += 1
        if data == 'clicked-link':
            player.link_clicks += 1


class Results(Page):
    pass


page_sequence = [MyPage, Results]
