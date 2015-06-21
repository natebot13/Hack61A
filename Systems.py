import pygame
from math import pi, sin, cos, atan2, degrees

class System:
    def SID(self):
        return self.__class__.__name__

class MovePlayer(System):
    operating_components = ['Player', 'Position', 'Velocity']
    def update(self, entityComponents):
        # print('Input xDir:', entityComponents['Input'].xDir)
        entityComponents['Position'].x += entityComponents['Velocity'].speed*cos(entityComponents['Velocity'].angle)
        entityComponents['Position'].y += entityComponents['Velocity'].speed*sin(entityComponents['Velocity'].angle)

class KeyboardInput(System):
    operating_components = ['Velocity']
    up, down = 0, 0
    left, right = 0, 0

    def update(self, entityComponents):
        # KEY CHECKS, EDIT AS NECESSARY #
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = -1
                if event.key == pygame.K_DOWN:
                    self.down = 1
                if event.key == pygame.K_LEFT:
                    self.left = -1
                if event.key == pygame.K_RIGHT:
                    self.right = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = 0
                if event.key == pygame.K_DOWN:
                    self.down = 0
                if event.key == pygame.K_LEFT:
                    self.left = 0
                if event.key == pygame.K_RIGHT:
                    self.right = 0
            x = self.left + self.right
            y = self.up + self.down
            if x == 0 and y == 0:
                entityComponents['Velocity'].speed = 0
            else:
                entityComponents['Velocity'].speed = entityComponents['Velocity'].spdCONST
                entityComponents['Velocity'].angle = atan2(y, x)

class Render(System):
    def __init__(self, screen):
        self.screen = screen
    operating_components = ['Renderable', 'Position', 'Velocity']
    def update(self, entityComponents):
        print(degrees(entityComponents['Velocity'].angle))
        if  pi/2 > entityComponents['Velocity'].angle > -pi/2:
            dirstr = 'R'
        else:
            dirstr = 'L'
        if entityComponents['Velocity'].angle < 0:
            dirstr += 'U'
        else:
            dirstr += 'D'
        self.screen.blit(entityComponents['Renderable'].images[dirstr], entityComponents['Position'].xy)

class FireballShooter(System):
    operating_components = ['Fireball', 'Shooter', 'Position']
    def __init__(self, entity_manager):
        self.entity_manager = entity_manager

    def update(self, entityComponents):
        pass

#### DO NOT EDIT BELOW THIS ####

class SystemsManager:
    def __init__(self, entity_manager, screen):
        self.entity_manager = entity_manager
        # BE SURE TO ADD ALL SYSTEMS TO THIS SYSTEM INIT LIST #
        self.registeredSystems = [MovePlayer(), KeyboardInput(), Render(screen)]
        # END SYS INIT LIST #

    def runSystems(self):
        for entity in self.entity_manager.allEntities():
            for system in self.registeredSystems:
                if self.entity_manager.entityHasComponents(entity, system.operating_components):
                    system.update(self.entity_manager.getEntity(entity))

    def registerSystem(self, system):
        self.registeredSystems.append(system())

    def allSystems(self):
        for system in registeredSystems:
            yield system