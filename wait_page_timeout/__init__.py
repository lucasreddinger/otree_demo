from otree.api import *

doc = """Timeout on a WaitPage (exit the experiment)"""

class C(BaseConstants):
    NAME_IN_URL = 'wait_page_timeout'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TIMEOUT = 15


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random

    for p in subsession.get_players():
        p.completion_code = random.randint(10 ** 6, 10 ** 7)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    timeout = models.FloatField()
    completion_code = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time

        # 15 seconds on wait page max
        player.timeout = time.time() + C.TIMEOUT


class ResultsWaitPage(WaitPage):
    template_name = 'wait_page_timeout/ResultsWaitPage.html'

    @staticmethod
    def js_vars(player: Player):
        return dict(timeout=C.TIMEOUT)

    @staticmethod
    def vars_for_template(player: Player):
        import time

        timeout_happened = time.time() > player.timeout
        return dict(timeout_happened=timeout_happened)


class Task(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Task]
