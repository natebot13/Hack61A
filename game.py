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
    entManager.addComponentToEntity(ID, Position())
    entManager.addComponentToEntity(ID, Velocity())
    entManager.addComponentToEntity(ID, Input())
    entManager.addComponentToEntity(ID, Renderable('Thing'))
    ID = entManager.newEntity()
    entManager.addComponentToEntity(ID, Position())

    while True:
        SCREEN.fill((0,0,0))
        sysManager.runSystems()
        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == "__main__":
    main()