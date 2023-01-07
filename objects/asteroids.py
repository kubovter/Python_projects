import pyglet as pg
from spaceship import Spaceship

objects = []
keys_pressed = set()
KEY_WIDTH = 800
KEY_HIGHT = 500
window = pg.window.Window(KEY_WIDTH,KEY_HIGHT)

def init_spaceship():
    spaceship = Spaceship()
    spaceship.x = window.width/2
    spaceship.y = window.height/2

    objects.append(spaceship)

def draw_objects():
    window.clear()

    for object in objects:
        object.draw()
            

def on_key_pressed(key,modifiers):
    keys_pressed.add(key)

def on_key_released(key,modifiers):
    keys_pressed.remove(key)

def tick_objects(t):
    for object in objects:
        object.tick(t,keys_pressed)

init_spaceship()
window.push_handlers(
    on_draw=draw_objects,
    on_key_press=on_key_pressed,
    on_key_release=on_key_released
    )

pg.clock.schedule_interval(tick_objects,1/30)

pg.app.run()