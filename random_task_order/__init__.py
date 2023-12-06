import random
from otree.api import *

doc = """
For each participant, randomize the order of tasks A, B, and C.
Task B has 2 pages, which are always shown in the same order.
The page_sequence contains all tasks;
in each round we show a randomly determined subset of pages.
"""


class C(BaseConstants):
    NAME_IN_URL = 'random_task_order'
    PLAYERS_PER_GROUP = None
    TASKS = ['A', 'B', 'C']
    NUM_ROUNDS = len(TASKS)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            task_rounds = dict(zip(C.TASKS, round_numbers))
            # print('player', p.id_in_subsession)
            # print('task_rounds is', task_rounds)
            p.participant.task_rounds = task_rounds


# PAGES
class TaskA(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['A']


class TaskB1(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B']


class TaskB2(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B']


class TaskC(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['C']


page_sequence = [
    TaskA,
    TaskB1,
    TaskB2,
    TaskC,
]
