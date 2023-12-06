from otree.api import *
import random

doc = """
custom_export: 1 row for each group
"""


class C(BaseConstants):
    NAME_IN_URL = 'custom_export'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    """generate some fake data for the export"""
    for g in subsession.get_groups():
        g.gfield1 = random.randint(0, 100)


class Group(BaseGroup):
    gfield1 = models.IntegerField()


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    pass


page_sequence = [MyPage]


def get_groups(players):
    """gets all groups that these players belong to, without duplicates"""
    already_added = set()
    groups = []
    for p in players:
        group = p.group
        if group.id not in already_added:
            already_added.add(group.id)
            groups.append(group)
    return groups


def custom_export(players):
    """
    Export 1 row for each group
    """
    yield ['session.code', 'round_number', 'group.id_in_subsession', 'group.gfield1']
    for g in get_groups(players):
        yield [g.session.code, g.round_number, g.id_in_subsession, g.gfield1]
