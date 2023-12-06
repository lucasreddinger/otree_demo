from otree.api import *

doc = """
Store the history of invalid responses a user made. 
"""


class C(BaseConstants):
    NAME_IN_URL = 'save_wrong_answers'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.IntegerField(label='What is 2 + 2?')
    quiz2 = models.StringField(
        label='What is the capital of Canada?',
        choices=['Ottawa', 'Toronto', 'Vancouver'],
    )
    quiz3 = models.IntegerField(label="What year did COVID-19 start?")
    quiz4 = models.BooleanField(label="Is 4 a prime number")


class IncorrectResponse(ExtraModel):
    player = models.Link(Player)
    field_name = models.StringField()
    response = models.StringField()


class MyPage(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=4, quiz2='Ottawa', quiz3=2019, quiz4=False)

        errors = {name: 'Try again' for name in solutions if values[name] != solutions[name]}
        if errors:
            for name in errors:
                response = values[name]
                IncorrectResponse.create(player=player, field_name=name, response=str(response))
            return errors


class Results(Page):
    pass


page_sequence = [MyPage, Results]


def custom_export(players):
    """For data export page"""

    yield ['participant_code', 'id_in_session', 'round_number', 'field_name', 'response']
    responses = IncorrectResponse.filter()

    for resp in responses:
        player = resp.player
        participant = player.participant
        yield [participant.code, participant.id_in_session, player.round_number, resp.field_name, resp.response]
