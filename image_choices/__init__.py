from otree.api import *


doc = """
Images in radio button choices
"""


def make_image_data(image_names):
    return [dict(name=name, path='shapes/{}'.format(name)) for name in image_names]


class C(BaseConstants):
    NAME_IN_URL = 'image_choices'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    img_choice = models.StringField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['img_choice']

    @staticmethod
    def vars_for_template(player: Player):
        image_names = [
            'circle-blue.svg',
            'plus-green.svg',
            'star-red.svg',
            'triangle-yellow.svg',
        ]
        return dict(image_data=make_image_data(image_names))


page_sequence = [MyPage]
