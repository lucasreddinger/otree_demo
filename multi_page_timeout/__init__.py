from otree.api import *

doc = """
Timeout spanning multiple pages
"""


class C(BaseConstants):
    NAME_IN_URL = 'multi_page_timeout'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIMER_TEXT = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()


def is_displayed1(player: Player):
    """only returns True if there is time left."""
    return get_timeout_seconds1(player) > 0


class Intro(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time

        participant.expiry = time.time() + 60


class Page1(Page):
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Page2(Page):
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = C.TIMER_TEXT


class Page3(Page):
    is_displayed = is_displayed1
    timer_text = C.TIMER_TEXT
    get_timeout_seconds = get_timeout_seconds1


page_sequence = [Intro, Page1, Page2, Page3]
