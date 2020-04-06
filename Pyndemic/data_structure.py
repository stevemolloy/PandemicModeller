class Node:
    '''
    The most basic element in the class hierarchy that will define
    the population tree of the model
    '''
    def __init__(self):
        self.children = []
        self.outgoing = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.parent})'


class HouseHold(Node):
    'The inputs should be of type SmallGroup'
    def __init__(self, kids, adults, retirees):
        super().__init__()
        self.kids = kids
        self.adults = adults
        self.retirees = retirees

    @property
    def population(self):
        kids = self.kids.population
        adults = self.adults.population
        retirees = self.retirees.population
        return kids + adults + retirees

    @property
    def number_sick(self):
        kids = self.kids.number_sick
        adults = self.adults.number_sick
        retirees = self.retirees.number_sick
        return kids + adults + retirees

    @property
    def fatality_rate(self):
        kids = self.kids.D
        adults = self.adults.D
        retirees = self.retirees.D
        return (kids + adults + retirees) / self.population

    def __repr__(self):
        classname = self.__class__.__name__
        kids = f'kids={self.kids}'
        adults = f'adults={self.adults}'
        retirees = f'retirees={self.retirees}'
        return f'{classname}({kids}, {adults}, {retirees})'


class Neighbourhood(Node):
    pass


class UrbanArea(Node):
    pass


class SmallGroup:
    def __init__(self, population):
        self.S = population # Susceptible
        self.E = 0 # Exposed (and therefore sick)
        self.I = 0 # Infectious (and therefore sick)
        self.R = 0 # Recovered (healthy and immune)
        self.D = 0 # Died

    @property
    def population(self):
        return self.S + self.E + self.I + self.R + self.D

    @property
    def number_sick(self):
        return self.E + self.I

    @property
    def number_immue(self):
        'Total recovered plus total dead'
        return self.R + self.D

    @property
    def fatality_rate(self):
        'Fraction of deaths from those who are or have been sick'
        return self.D / (self.population() - self.S)

    def expose(self):
        if self.S <= 0:
            raise ValueError('No susceptible people in the group')
        self.S -= 1
        self.E += 1

    def become_infectious(self):
        if self.E <= 0:
            raise ValueError('No exposed people in the group')
        self.E -= 1
        self.I += 1

    def recover(self):
        if self.I <= 0:
            raise ValueError('No infectious people in the group')
        self.I -= 1
        self.R += 1

    def die(self):
        if self.I <= 0:
            raise ValueError('No infectious people in the group')
        self.I -= 1
        self.D += 1

