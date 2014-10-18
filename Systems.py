import pygame

class System:
    def SID(self):
        return self.__class__.__name__

class MovePlayer(System):
    operating_components = ['Position', 'Velocity', 'Input']
    def update(self, entityComponents):
        print('Input xDir:', entityComponents['Input'].xDir)
        entityComponents['Position'].x += entityComponents['Velocity'].vel*entityComponents['Input'].xDir
        entityComponents['Position'].y += entityComponents['Velocity'].vel*entityComponents['Input'].yDir

class KeyboardInput(System):
    operating_components = ['Input']
    up, down = 0, 0

    def update(self, entityComponents):
        # KEY CHECKS, EDIT AS NECESSARY #
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up = 1
                if event.key == pygame.K_DOWN:
                    self.down = -1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up = 0
                if event.key == pygame.K_DOWN:
                    self.down = 0
            print('Up and Down:', self.up, self.down)
            entityComponents['Input'].yDir = self.up + self.down
            # For Now!
            entityComponents['Input'].xDir = 0

class Render(System):
    def __init__(self, screen):
        self.screen = screen
    operating_components = ['Renderable', 'Position']
    def update(self, entityComponents):
        entityComponents['Renderable'].image.blit(self.screen, entityComponents['Position'].xy)

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