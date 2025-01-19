from pygame import *
class Sprite():
    def __init__(self, x, y, picture):
        self.rect = picture.get_rect() # скопированная строчка
        self.rect.x = x
        self.rect.y = y
        self.picture = picture

    def draw(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))
    
window = display.set_mode((900, 600))
window.fill((130, 242, 252))

ball_picture = transform.scale(image.load('medicine-ball.png'), (60, 60))
ball = Sprite(450, 250, ball_picture)

racket1_picture = transform.scale(image.load('rectangle.png'), (60, 140))
racket1 = Sprite(30, 250, racket1_picture)

racket2_picture = transform.scale(image.load('rectangle.png'), (60, 140))
racket2 = Sprite(820, 250, racket1_picture)

FPS = 60
clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    ball.draw()
    racket1.draw()
    racket2.draw()

    display.update()
    clock.tick(FPS)
