import pygame
import sys
from pygame.locals import *

pygame.init()

# assign FPS value
FPS = 30
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen_size = (300, 300)


DISPLAYSURF = pygame.display.set_mode(screen_size)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("face")


pygame.draw.line(DISPLAYSURF, BLUE, (300, 300), (0, 0))
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 300),23)
pygame.draw.circle(DISPLAYSURF, RED, (0, 0),23)


while True:
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)
