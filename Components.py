import pygame

class Component:
    def CID(self):
        return self.__class__.__name__

class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def xy(self):
        return (self.x,self.y)

class Velocity(Component):
    def __init__(self, speed=5):
        self.spdCONST = speed
        self.speed = 0
        self.angle = 0

class Renderable(Component):
    def __init__(self, filename, multidir=True):
        self.images = {}
        if multidir:
            directions = ['RU', 'LU', 'LD', 'RD']
            for i in range(1,5):
                self.images[directions[i-1]] = pygame.image.load(filename + '_' + str(i) + '.png')
        else:
            self.images = pygame.image.load(filename + '.png')

class Fireball(Component):
    def __init__(self):
        pass

class Shooter(Component):
    def __init__(self):
        pass

class Unique(Component):
    def __init__(self):
        pass