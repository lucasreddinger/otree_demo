from otree.api import *


doc = """
An image that changes when you move a slider.
If your image is a some kind of chart, it's better to use Highcharts than static images.
See the SVO example.
"""


class C(BaseConstants):
    NAME_IN_URL = 'slider_graphic'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    feeling = models.IntegerField(min=0, max=3)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['feeling']

    @staticmethod
    def vars_for_template(player: Player):
        img_paths = ['slider_graphic/{}.svg'.format(i) for i in range(4)]
        return dict(img_paths=img_paths)


page_sequence = [MyPage]
