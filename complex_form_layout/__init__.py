from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'complex_form_layout'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    a1 = models.IntegerField()
    a2 = models.IntegerField()
    a3 = models.IntegerField()
    a4 = models.IntegerField()

    b1 = models.StringField()
    b2 = models.StringField()
    b3 = models.StringField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3']

    @staticmethod
    def vars_for_template(player: Player):
        import random

        a_fields = ['a1', 'a2', 'a3', 'a4']
        b_fields = ['b1', 'b2', 'b3']

        random.shuffle(a_fields)
        random.shuffle(b_fields)

        return dict(a_fields=a_fields, b_fields=b_fields)


page_sequence = [MyPage]
