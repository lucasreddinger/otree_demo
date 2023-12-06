from otree.api import *


doc = """
Wait only for specific people
"""


class C(BaseConstants):
    NAME_IN_URL = 'wait_for_specific_people'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    import random

    session.wait_for_ids = set()
    session.arrived_ids = set()

    for p in subsession.get_players():
        # we just determine it randomly here.
        # in your game, you should replace it with your desired logic.
        selected = random.choice([False, True])
        p.selected_for_waitpage = selected
        if selected:
            session.wait_for_ids.add(p.id_in_subsession)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    selected_for_waitpage = models.BooleanField()


class Intro(Page):
    pass


class WaitForSelected(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.selected_for_waitpage

    @staticmethod
    def live_method(player: Player, data):
        session = player.session
        session.arrived_ids.add(player.id_in_subsession)
        not_arrived_yet = session.wait_for_ids - session.arrived_ids
        if not_arrived_yet:
            return {0: dict(not_arrived_yet=list(not_arrived_yet))}
        return {0: dict(finished=True)}

    @staticmethod
    def error_message(player: Player, values):
        session = player.session
        if session.arrived_ids != session.wait_for_ids:
            return "Page somehow proceeded before all players are ready"


class Results(Page):
    pass


page_sequence = [Intro, WaitForSelected, Results]
