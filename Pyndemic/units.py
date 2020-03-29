"""
Basic units used in the pandemic modelling
"""

from collections import namedtuple

class HouseHold:
    def __init__(self, kids, adults, retirees):
        Members = namedtuple('Members', 'kids adults retirees')
        self.members = Members(kids=kids, adults=adults, retirees=retirees)
        self.exposed = Members(kids=0, adults=0, retirees=0)
        self.infectious = Members(kids=0, adults=0, retirees=0)
        self.recovered = Members(kids=0, adults=0, retirees=0)

    def infect(self, kids, adults, retirees):
        infected_kids = self.infected.kids + kids
        infected_adults = self.infected.adults + adults
        infected_retirees = self.infected.retirees + retirees
