from Systems import *
from EntityManager import *
from Components import *
import pygame

def main():
    WIDTH = 512
    HEIGHT = 512
    SIZE = (WIDTH,HEIGHT)
    FPS = 60
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Hack61A")
    CLOCK = pygame.time.Clock()

    entManager = EntityManager()
    sysManager = SystemsManager(entManager, SCREEN)
    ID = entManager.newEntity()
    entManager.addComponentToEntity(ID, Position(100, 100))
    entManager.addComponentToEntity(ID, Velocity())
    entManager.addComponentToEntity(ID, Fireball())
    entManager.addComponentToEntity(ID, Shooter())
    entManager.addComponentToEntity(ID, Renderable('data/graphics/Thing'))
    # ID = entManager.newEntity()
    # entManager.addComponentToEntity(ID, Position())

    while True:
        SCREEN.fill((255,255,255))
        sysManager.runSystems(CLOCK.get_time())
        pygame.display.update()
        CLOCK.tick(FPS)
        sysManager.endStep()

if __name__ == "__main__":
    main()