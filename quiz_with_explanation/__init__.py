from otree.api import *


doc = """
Quiz with explanation. Re-display the previous page's form as read-only, with answers/explanation.
"""


class C(BaseConstants):
    NAME_IN_URL = 'quiz_with_explanation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


def get_quiz_data():
    return [
        dict(
            name='a',
            solution=True,
            explanation="3 is prime. It has no factorization other than 1 and itself.",
        ),
        dict(
            name='b',
            solution=False,
            explanation="2 + 2 is 4.",
        ),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    a = models.BooleanField(label="Is 3 a prime number?")
    b = models.IntegerField(label="What is 2 + 2?")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['a', 'b']

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_quiz_data()
        return dict(fields=fields, show_solutions=False)


class Results(Page):
    form_model = 'player'
    form_fields = ['a', 'b']

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_quiz_data()
        # we add an extra entry 'is_correct' (True/False) to each field
        for d in fields:
            d['is_correct'] = getattr(player, d['name']) == d['solution']
        return dict(fields=fields, show_solutions=True)

    @staticmethod
    def error_message(player: Player, values):
        for field in values:
            if getattr(player, field) != values[field]:
                return "A field was somehow changed but this page is read-only."


page_sequence = [MyPage, Results]
