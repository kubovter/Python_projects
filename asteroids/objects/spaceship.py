import pyglet as pg
import math

ROTATION_SPEED = 2  # radians per second
ACCELERATION = 100

class Spaceship:

    batch = pg.graphics.Batch() #batch na obrazky(sprity)
    # konstruktor na raketku se souradnicemi a obrazkem
    def __init__(self):
        self.x = 0 #pozice
        self.y = 0
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        image = pg.image.load('playerShip2_red.png')
        image.anchor_x = image.width // 2 #nastavi raketku na stred
        image.anchor_y = image.height // 2
        self.sprite = pg.sprite.Sprite(image,batch=self.batch) #2D objekt v Pygletu

    # metoda na vykresleni raketky
    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - math.degrees(self.rotation) #aby se pohyb promitl do raketky
        self.sprite.draw()

    # metoda na pohyb
    def tick(self,t,key_pressed):
        if pg.window.key.LEFT in key_pressed:
            self.rotation += t*ROTATION_SPEED # + je jako pohyb doleva
            self.x_speed = 10
            self.y_speed = 10
            self.x_speed += t * ACCELERATION * math.cos(self.rotation)
            self.y_speed += t * ACCELERATION * math.sin(self.rotation)
        if pg.window.key.RIGHT in key_pressed:
            self.rotation = self.rotation - t*ROTATION_SPEED # - jako pohyb doprava
            self.x_speed = 10
            self.y_speed = 10
            self.x_speed += t * ACCELERATION * math.cos(self.rotation)
            self.y_speed += t * ACCELERATION * math.sin(self.rotation)
        if pg.window.key.UP in key_pressed:
            self.x_speed += t * ACCELERATION * math.cos(self.rotation)
            self.y_speed += t * ACCELERATION * math.sin(self.rotation)
        if pg.window.key.DOWN in key_pressed:
            self.x_speed += t * -1 * ACCELERATION * math.cos(self.rotation)
            self.y_speed += t * -1 * ACCELERATION * math.sin(self.rotation)

        self.x = self.x + t * self.x_speed #pohyb
        self.y = self.y + t * self.y_speed
        
        if self.x > 800:
            self.x = 0
        if self.y > 500:
            self.y = 0