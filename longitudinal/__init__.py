from otree.api import *


doc = """
Longitudinal study (2-part study taking place across days/weeks)

Another way to do longitudinal studies is just to give participants a Room URL.
Since that URL is persistent, you can create a new session when the next phase has begun.

But the technique here has the advantage of storing both phases together in a single session.
For example, you can easily compare the user's answer to their answer in the previous phase.
"""


class C(BaseConstants):
    NAME_IN_URL = 'longitudinal'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    question = models.StringField()
    part2_start_time = models.FloatField()
    part2_start_time_readable = models.StringField()


# PAGES
class Part1(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        from datetime import datetime, timedelta

        t = datetime.now() + timedelta(weeks=1)
        # or can make it for a specific date:
        # start = datetime.strptime('2022-07-15', '%Y-%m-%d')

        # .timestamp() gives you an integer (a.k.a. 'epoch time')
        player.part2_start_time = t.timestamp()
        # print('player.part2_start_time is', player.part2_start_time)
        # this gives you a formatted date you can display to users
        player.part2_start_time_readable = t.strftime('%A, %B %d')


def still_waiting_for_part_2(player: Player):
    import time

    # returns True if the current time is before the designated start time
    return time.time() < player.part2_start_time


class Bridge(Page):
    """
    If the user arrives at this page after part 2 is ready, this page will
    be skipped entirely.
    """

    @staticmethod
    def is_displayed(player: Player):
        return still_waiting_for_part_2(player)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        return "Player somehow tried to proceed past a page with no next button"


class Part2(Page):
    pass


page_sequence = [Part1, Bridge, Part2]
