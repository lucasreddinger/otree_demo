from otree.api import *




class C(BaseConstants):
    NAME_IN_URL = 'redirect_to_other_website'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    citizenship = models.StringField()



class MyPage(Page):
    form_model = 'player'
    form_fields = ['citizenship']


class Redirect(Page):
    @staticmethod
    def js_vars(player: Player):
        # google is just an example. you should change this to qualtrics or whatever survey provider
        # you are using.
        return dict(redirect_url='https://www.google.com/search?q=' + player.citizenship)


page_sequence = [MyPage, Redirect]
