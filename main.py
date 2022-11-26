import pygame
import os
pygame.init()
pygame.font.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (w,h))
        self.w = w
        self.h = h 
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = pygame.Rect(x,y, w,h)

    def show(self):
        window.blit(self.image, (self.x, self.y))


class Racket(GameSprite):
    def __init__(self, image, w,h, x,y, speed, keyup, keydown):
        super().__init__(image, w,h, x,y, speed)
        self.keyup = keyup
        self.keydown = keydown
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.keydown] == True and self.rect.y < window_h- 200:
            self.y += self.speed
        if keys[self.keyup] == True and self.rect.y > 0:
            self.y -= self.speed
        self.rect.y = self.y
        
class Ball(GameSprite):
    def __init__(self, image, w,h, x,y, speed):
        super().__init__(image, w,h, x,y, speed)
        self.directX = 1
        self.directY = 1


    def move(self):
        global right_m
        global left_m
        self.x += self.speed*self.directX
        self.y += self.speed*self.directY

        if self.rect.y >= window_h - 50:
            self.directY = -1
        elif self.rect.y <= 0:
            self.directY = 1

        if self.rect.x >= window_w - 50:
            self.directX = -1
            right_m += 1

        elif self.rect.x <= 0:
            self.directX = 1
            left_m += 1

        self.rect.x = self.x
        self.rect.y = self.y

    def colid_result(self):
        self.directX *= -1

PATH= os.path.dirname(__file__) + os.sep
font = pygame.font.Font(PATH+'Roboto-Bold.ttf', 120)
window_w = 1280
window_h = 720
window = pygame.display.set_mode((window_w, window_h))
tik = pygame.time.Clock()
game = True
right_m = 0
left_m = 0


platform0 = Racket(PATH+'platform0.png', 30, 200, 10, 10, 10, pygame.K_w, pygame.K_s)
platform1 = Racket(PATH+'platform1.png', 30, 200, window_w-40, window_h-210, 10, pygame.K_UP, pygame.K_DOWN)
ball = Ball(PATH+"ball.png", 50,50, 635, 300, 7.5)
background0 = GameSprite(PATH+'Background_2.png', window_w, window_h, 0, 0, 0)


while game:
    background0.show()

    text = font.render(str(int(right_m/3)),1, (179, 179, 0))
    text1 = font.render(str(int(left_m/3)),1, (255, 51, 153))

    window.blit(text, (100, 0))
    window.blit(text1, (window_w-200, 0))

    platform1.move()
    platform1.show()

    platform0.move()
    platform0.show()

    ball.show()
    ball.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if pygame.sprite.collide_rect(ball, platform1):
        ball.colid_result()

    if pygame.sprite.collide_rect(ball, platform0):
        ball.colid_result()

    tik.tick(30)
    pygame.display.update()
