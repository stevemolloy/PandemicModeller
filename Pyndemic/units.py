"""
Basic units used in the pandemic modelling
"""

from collections import namedtuple
Members = namedtuple('Members', 'kids adults retirees')

class HouseHold:
    def __init__(self, kids, adults, retirees):
        self.members = Members(kids=kids, adults=adults, retirees=retirees)
        self.S = Members(kids=kids, adults=adults, retirees=retirees)
        self.E = Members(kids=0, adults=0, retirees=0)
        self.I = Members(kids=0, adults=0, retirees=0)
        self.R = Members(kids=0, adults=0, retirees=0)

    def infect(self, kids, adults, retirees):
        self.E = Members(
                kids=self.E.kids + kids,
                adults=self.E.adults + adults,
                retirees=self.E.retirees + retirees,
            )

