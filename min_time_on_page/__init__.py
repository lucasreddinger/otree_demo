from otree.api import *


doc = """
Minimum time on a page
"""


class C(BaseConstants):
    NAME_IN_URL = 'min_time_on_page'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    pass


class Player(BasePlayer):
    page_pass_time = models.FloatField()


class Page1(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time

        player.page_pass_time = time.time() + 10


# PAGES
class Page2(Page):
    @staticmethod
    def error_message(player: Player, values):
        import time

        if time.time() < player.page_pass_time:
            return "You cannot pass this page yet."


class Page3(Page):
    pass


page_sequence = [Page1, Page2, Page3]
