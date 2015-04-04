import os, sys
import pygame
import langton

class LangtonGame(object):
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        self.world = langton.World()

    def main_loop(self):
        BLACK = (0,0,0)
        GREEN = (0,255,0)

        x_offset = 420
        y_offset = 340
        cellsize = 2

        while 1:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for i in self.world.grid:
                r = pygame.Rect(i.x * cellsize + x_offset, i.y * cellsize + y_offset, cellsize, cellsize)
                pygame.draw.rect(self.screen, GREEN, r)
            
            pygame.display.update()
            self.world.run()


if __name__ == "__main__":
    mainwindow = LangtonGame()
    mainwindow.main_loop()