"""
Basic units used in the pandemic modelling
"""

from random import random


class People:
    def __init__(self, kids, adults, retirees):
        self.kids = kids
        self.adults = adults
        self.retirees = retirees

    def __repr__(self):
        k = self.kids
        a = self.adults
        r = self.retirees
        return f'People(kids={k}, adults={a}, retirees={r})'


class HouseHold:
    def __init__(self, kids, adults, retirees):
        self.members = People(kids=kids, adults=adults, retirees=retirees)
        self.S = People(kids=kids, adults=adults, retirees=retirees)
        self.E = People(kids=0, adults=0, retirees=0)
        self.I = People(kids=0, adults=0, retirees=0)
        self.R = People(kids=0, adults=0, retirees=0)
        self.D = People(kids=0, adults=0, retirees=0)

    def infect(self, kids, adults, retirees):
        self.S.kids -= kids
        self.S.adults -= adults
        self.S.retirees -= retirees

        self.E.kids += kids
        self.E.adults += adults
        self.E.retirees += retirees

    def step_time(self, become_infectious=0.05):
        for i in range(self.E.kids):
            if random() < become_infectious:
                self.E.kids -= 1
                self.I.kids += 1

        for i in range(self.E.adults):
            if random() < become_infectious:
                self.E.adults -= 1
                self.I.adults += 1

        for i in range(self.E.retirees):
            if random() < become_infectious:
                self.E.retirees -= 1
                self.I.retirees += 1

    def __repr__(self):
        k = self.members.kids
        a = self.members.adults
        r = self.members.retirees
        return f'HouseHold(kids={k}, adults={a}, retirees={r})'

