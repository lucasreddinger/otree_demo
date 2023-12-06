from appcopy1 import *


class C(C):
    NAME_IN_URL = 'appcopy2'


# need to copy/paste Subsession/Group/Player classes from appcopy1
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    aaa = models.IntegerField()


class Player(BasePlayer):
    bbb = models.IntegerField()
