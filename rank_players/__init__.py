from otree.api import *


doc = """
Rank players
"""


class C(BaseConstants):
    NAME_IN_URL = 'rank_players'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="Enter your age")
    rank = models.IntegerField()


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['age']


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        players = group.get_players()
        # to do descending, use -p.age
        players.sort(key=lambda p: p.age)
        for i in range(len(players)):
            # this code checks if there is a tie and then assigns the same rank
            # if you don't need to deal with ties, then you can delete this.
            if i > 0 and players[i].age == players[i - 1].age:
                rank = players[i - 1].rank
            else:
                rank = i + 1
            players[i].rank = rank


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(num_players=len(group.get_players()))


page_sequence = [MyPage, ResultsWaitPage, Results]
