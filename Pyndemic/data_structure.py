class Node:
    def __init__(self):
        self.children = []
        self.outgoing = []
        self.parent = None
        self.data = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.parent})'

class Neighbourhood(Node):
    pass

class UrbanArea(Node):
    pass

