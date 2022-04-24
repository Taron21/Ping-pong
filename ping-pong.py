from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width=65, height=65):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (width, height))
         self.speed = player_speed
         self.rect = self.image .get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 495:
            self.rect.y += self.speed

finish = False
FPS = 60
clock = time.clock()

window = display.set_mode((700, 500))
display.set_caption('Ping-pong')
fon = transform.scale(image.load('back.jpg'), (700, 500))

player = Player('rack.jpg', 20, 250, 3)

while finish != True:
    for e in event.get():
        if e.type == QUIT:
            game = True
display.update()
clock.tick(FPS)