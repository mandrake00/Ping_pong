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
        window.blit(pygame.image.load(self.image), (self.x, self.y))


class Racket(GameSprite):
    def __init__(self, image, w,h, x,y, speed, keyup, keydown):
        super().__init__(image, w,h, x,y, speed)
        self.keyup = keyup
        self.keydown = keydown
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.keydown] == True:
            self.y += self.speed
        if keys[self.keyup] == True:
            self.y -= self.speed
        self.rect.y = self.y
        
class Ball(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)

platform1 = Racket(PATH+'platform_placeholder.jpeg', 10, 100, 10, 10, 10, pygame.K_w, pygame.K_s)
platform2 = Racket(PATH+'platform_placeholder.jpeg', 10, 100, window_w-40, window_h-210, 10, pygame.K_UP, pygame.K_DOWN)

while game:
    window.blit(pygame.transform.scale(pygame.image.load(PATH+'a.png'), (window_w, window_h)), (0,0))

    platform1.move()
    platform1.show()

    platform2.move()
    platform2.show()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    tik.tick(30)
    pygame.display.update()
