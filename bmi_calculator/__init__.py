from otree.api import *


doc = """
Basic single-player game (BMI calculator)
"""


class C(BaseConstants):
    NAME_IN_URL = 'bmi_calculator'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    weight_kg = models.IntegerField(label="Weight (in kg)")
    height_cm = models.IntegerField(label="Height (in cm)")
    bmi = models.FloatField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['weight_kg', 'height_cm']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        bmi = player.weight_kg / ((player.height_cm / 100) ** 2)
        player.bmi = round(bmi, 1)


class Results(Page):
    pass


page_sequence = [MyPage, Results]
