import pygame
import os
pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 70)

PATH= os.path.dirname(__file__) + os.sep

window_w = 1280
window_h = 720

window = pygame.display.set_mode((window_w, window_h))

tik = pygame.time.Clock()
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    tik.tick(30)
    pygame.display.update()