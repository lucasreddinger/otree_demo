from otree.api import *


doc = """
Using getattr() and setattr() to access numbered fields, e.g. 
player.num1, player.num2, ..., player.num10,
without writing repetitive if-statements.

NOTE: having numbered fields is often not the best or easiest design.
For example, let's say you have fields like this:

    num1 = models.IntegerField()
    num2 = models.IntegerField()
    ...
    num10 = models.IntegerField()

If you don't need to put them in a form, then you can replace this simply with 
a list in a participant field, since they can be more easily accessed by number, 
e.g. participant.my_numbers[5]

If you have many numbered fields, like more than 20, you should consider using 
ExtraModel.

Participant fields and ExtraModel also have the advantage that you don't need to know in
advance exactly how many you will have.
"""


class C(BaseConstants):
    NAME_IN_URL = 'getattr_setattr'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
    num4 = models.IntegerField()
    num5 = models.IntegerField()
    num6 = models.IntegerField()
    num7 = models.IntegerField()
    num8 = models.IntegerField()
    num9 = models.IntegerField()
    num10 = models.IntegerField()

    chosen_number = models.IntegerField(
        choices=C.NUMBERS, label="Choose a random number from 1 to 10"
    )


class Page1(Page):
    form_model = 'player'
    form_fields = ['num{}'.format(n) for n in C.NUMBERS]


class Page2(Page):
    form_model = 'player'
    form_fields = ['chosen_number']


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        # if chosen_number was 7, this will give you player.num7
        field_name = 'num{}'.format(player.chosen_number)
        chosen_value = getattr(player, field_name)
        player.payoff = chosen_value

        # if chosen number was 7, this gives you
        # player.num1 + player.num2 + ... + player.num7
        sum_to_n = sum(
            getattr(player, 'num{}'.format(n))
            for n in range(1, player.chosen_number + 1)
        )
        return dict(chosen_value=chosen_value, sum_to_n=sum_to_n)


page_sequence = [Page1, Page2, Results]
