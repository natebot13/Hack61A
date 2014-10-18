import pygame

class Component:
    def CID(self):
        return self.__class__.__name__

class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @property
    def xy():
        return (x,y)

class Velocity(Component):
    def __init__(self, vel=5):
        self.vel = vel

class Input(Component):
    def __init__(self):
        self.xDir = 0
        self.yDir = 0

class Renderable(Component):
    def __init__(self, filename):
        self.image = pygame.image.load(filename)

class Unique(Component):
    def __init__(self):
        pass

