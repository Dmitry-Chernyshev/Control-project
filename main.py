from pygame import *

class Sprite():
    def __init__(self, x, y, picture, speed = 10):
        self.rect = picture.get_rect() # скопированная строчка
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.picture = picture

    def draw(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))

    def control(self, key_up, key_down):
        keys = key.get_pressed()
        if keys[key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        elif keys[key_down] and self.rect.bottom < window.get_height():  #(window.get_height() - self.rect.height)
            self.rect.y += self.speed

class Ball(Sprite):
    def __init__(self, x, y, picture, speed, dir_x, dir_y):
        super().__init__(x, y, picture, speed)
        self.dir_x = dir_x
        self.dir_y = dir_y

    def move(self):
        self.rect.y += self.speed * self.dir_y
        self.rect.x += self.speed * self.dir_x
        if self.rect.bottom > window.get_height():
            self.dir_y = -self.dir_y
        if self.rect.y < 0:
            self.dir_y = -self.dir_y
        if sprite.collide_rect(self, racket1):
            self.dir_x = 1
        if sprite.collide_rect(self, racket2):
            self.dir_x = -1

ball_picture = transform.scale(image.load('medicine-ball.png'), (60, 60))
racket1_picture = transform.scale(image.load('rectangle.png'), (60, 140))
racket2_picture = transform.scale(image.load('rectangle.png'), (60, 140))

def start_game():
    global ball, racket1, racket2, mode
    ball = Ball(450, 250, ball_picture, 3, -1, 1)
    racket1 = Sprite(30, 250, racket1_picture)
    racket2 = Sprite(820, 250, racket1_picture)
    mode = 0
 
font.init()
font1 = font.Font(None, 50)
lose1 = font1.render('PLAYER 1 LOSE!', True, 'black')
lose2 = font1.render('PLAYER 2 LOSE!', True, 'black')
start_game()

window = display.set_mode((900, 600))
window.fill((130, 242, 252))

FPS = 60
clock = time.Clock()
run = True
mode = 0
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                if mode != 0:
                    start_game()
                    

        

    if mode == 0:
        racket1.control(K_w, K_s)
        racket2.control(K_UP, K_DOWN)
        ball.move()

    if ball.rect.x < 0:
        mode = 1
    elif ball.rect.x + ball.rect.width > window.get_width():
        mode = 2


    window.fill((130, 242, 252))
    if mode == 1:
        window.blit(lose1, (300, 250))
    elif mode == 2:
        window.blit(lose2, (300, 250))
    ball.draw()
    racket1.draw()
    racket2.draw()

    display.update()
    clock.tick(FPS)
