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

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__()
        self.image = image
        self.w = w
        self.h = h 
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x,y, w,h)

    def show(self):
        window.blit(pygame.transform.scale(pygame.image.load(self.image), (self.w, self.h)), (self.x, self.y))


class Racket(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        
    def ws(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] == True:
            self.rect.y += self.speed
        if keys[pygame.K_UP] == True:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    tik.tick(30)
    pygame.display.update()
