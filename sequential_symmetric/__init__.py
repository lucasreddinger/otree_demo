from otree.api import *


doc = """
Sequential / cascade game (symmetric).
Also see "intergenerational" featured app.
"""


class C(BaseConstants):
    NAME_IN_URL = 'sequential_symmetric'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    MAIN_TEMPLATE = __name__ + '/Decide.html'
    FORM_FIELDS = ['decision']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.IntegerField(
        label="How many countries are there in Africa? (Make your best guess)"
    )


def vars_for_template1(player: Player):
    return dict(
        # get the players whose ID is less than mine
        players=[
            p
            for p in player.get_others_in_group()
            if p.id_in_group < player.id_in_group
        ]
    )


# PAGES
class P1(Page):
    form_model = 'player'
    form_fields = C.FORM_FIELDS
    template_name = C.MAIN_TEMPLATE

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    vars_for_template = vars_for_template1


class WaitPage1(WaitPage):
    pass


class P2(Page):
    form_model = 'player'
    form_fields = C.FORM_FIELDS
    template_name = C.MAIN_TEMPLATE

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    vars_for_template = vars_for_template1


class WaitPage2(WaitPage):
    pass


class P3(Page):
    form_model = 'player'
    form_fields = C.FORM_FIELDS
    template_name = C.MAIN_TEMPLATE

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 3

    vars_for_template = vars_for_template1


class WaitPage3(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(players=group.get_players())


page_sequence = [P1, WaitPage1, P2, WaitPage2, P3, WaitPage3, Results]
