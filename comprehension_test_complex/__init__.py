from otree.api import *

doc = """
Comprehension test. If the user fails too many times, they exit.
"""


class C(BaseConstants):
    NAME_IN_URL = 'comprehension_test_complex'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.IntegerField(label='What is 2 + 2?')
    quiz2 = models.StringField(
        label='What is the capital of Canada?',
        choices=['Ottawa', 'Toronto', 'Vancouver'],
    )
    quiz3 = models.IntegerField(label="What year did COVID-19 start?")
    quiz4 = models.BooleanField(label="Is 9 a prime number")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    @staticmethod
    def error_message(player: Player, values):
        # alternatively, you could make quiz1_error_message, quiz2_error_message, etc.
        # but if you have many similar fields, this is more efficient.
        solutions = dict(quiz1=4, quiz2='Ottawa', quiz3=2019, quiz4=False)

        # error_message can return a dict whose keys are field names and whose
        # values are error messages
        errors = {name: 'Wrong' for name in solutions if values[name] != solutions[name]}
        # print('errors is', errors)
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 3:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors


class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many


class Results(Page):
    pass


page_sequence = [MyPage, Failed, Results]
