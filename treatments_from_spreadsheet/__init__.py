from otree.api import *


doc = """
Reading treatment parameters from a CSV spreadsheet
"""


class C(BaseConstants):
    NAME_IN_URL = 'treatments_from_spreadsheet'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import csv

    f = open(__name__ + '/treatments.csv', encoding='utf-8-sig')

    rows = list(csv.DictReader(f))
    players = subsession.get_players()
    for i in range(len(players)):
        row = rows[i]
        player = players[i]
        # CSV contains all data in string form, so we need to convert
        # to the correct data type, e.g. '1' -> 1 -> True.
        player.time_pressure = bool(int(row['time_pressure']))
        player.high_tax = bool(int(row['high_tax']))
        player.endowment = cu(row['endowment'])
        player.color = row['color']


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_pressure = models.BooleanField()
    endowment = models.CurrencyField()
    high_tax = models.BooleanField()
    color = models.StringField()


class MyPage(Page):
    pass


page_sequence = [MyPage]
