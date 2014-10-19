import pygame

class Component:
    def CID(self):
        return self.__class__.__name__

class Position(Component):
    def __init__(self, x=200, y=200):
        self.x = x
        self.y = y
    
    @property
    def xy(self):
        return (self.x,self.y)

class Velocity(Component):
    def __init__(self, vel=5):
        self.vel = vel

class Input(Component):
    def __init__(self):
        self.xDir = 0
        self.yDir = 0

class Renderable(Component):
    def __init__(self, filename, multidir=True):
        self.images = {}
        if multidir:
            directions = ['RU', 'LU', 'LD', 'RD']
            for i in range(1,5):
                self.images[directions[i-1]] = pygame.image.load(filename + '_' + str(i) + '.png')
        else:
            self.images = pygame.image.load(filename + '.png')

class Unique(Component):
    def __init__(self):
        pass

