 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import pyglet
window = pyglet.window.Window()
# Image resource folder
pyglet.resource.path.append('./image')
pyglet.resource.reindex()
# Load planet image
def center_anchor(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

planet_image = pyglet.resource.image('test.jpg')
center_anchor(planet_image)

class Planet(pyglet.sprite.Sprite):
    def __init__(self, image, x=0, y=0, batch=None):
        super(Planet, self).__init__(image, x, y, batch=batch)
        self.x = x
        self.y = y
cneter_x = int(window.width/2)
cneter_y = int(window.height/2)
planet = Planet(planet_image, cneter_x, cneter_y, None)

@window.event
def on_draw():
    window.clear()
    planet.draw()

pyglet.app.run()