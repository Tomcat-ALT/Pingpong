from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, img, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class player(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <  win_h-80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <  win_h-80:
            self.rect.y += self.speed


back = (200, 255, 255)
win_w = 600
win_h = 500
window = display.set_mode((win_w, win_h))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 60

r1 = player(r'/Users/rifki/.vscode/extensions/algoritmika.algopython-20241210.135312.0/temp/Ping Pong/racket.png', 30, 200, 4, 50, 150)
r2 = player(r'/Users/rifki/.vscode/extensions/algoritmika.algopython-20241210.135312.0/temp/Ping Pong/racket.png', 520, 200, 4, 50, 150)
ball = Gamesprite(r'/Users/rifki/.vscode/extensions/algoritmika.algopython-20241210.135312.0/temp/Ping Pong/tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))


speed_x = 3
speed_y = 3

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
   if finish != True:
       window.fill(back)
       r1.update_l()
       r2.update_r()
       ball.rect.x += speed_x
       ball.rect.y += speed_y
       if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
           speed_x *= -1
           speed_y *= 1
       if ball.rect.y > win_h-50 or ball.rect.y < 0:
           speed_y *= -1
       if ball.rect.x < 0:
           finish = True
           window.blit(lose1, (200, 200))
           game_over = True
       if ball.rect.x > win_w:
           finish = True
           window.blit(lose2, (200, 200))
           game_over = True
       r1.reset()
       r2.reset()
       ball.reset()
   display.update()
   clock.tick(fps)