import os, sys
import pygame
import hexs
import random


class HexGame(object):
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        #self.world = hexs.World()
        cells = []
        
        for i in range(400):
            cells.append([random.randint(0, 40), random.randint(0, 40)])

        self.world = hexs.World(cells)

    def main_loop(self):
        BLACK = (0,0,0)
        GREEN = (0,255,0)

        x_offset = 0
        y_offset = 0
        cellsize = 15

        clock = pygame.time.Clock()

        while 1:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for i in self.world.cells:
                #r = pygame.Rect(i[0] * cellsize + x_offset, i[1] * cellsize + y_offset, cellsize, cellsize)
                #pygame.draw.rect(self.screen, GREEN, r)
                odd_offset = 0
                if i[1] % 2 > 0:
                    odd_offset = cellsize
                
                pygame.draw.circle(self.screen, GREEN, (i[0] * cellsize + x_offset - (odd_offset / 2), i[1] * cellsize + y_offset), cellsize - 5, 1)
            
            pygame.display.update()
            self.world.run()
            clock.tick(1)


if __name__ == "__main__":
    mainwindow = HexGame()
    mainwindow.main_loop()
