import pygame as py
from enum import Enum
# pygame setup
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True
dt = 0

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class Player:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    # Cooperate means take step(s) forward
    def coop(self):
        if self.direction == Direction.LEFT: 
            self.x = self.x - (screen.getwidth()/5)
        if self.direction == Direction.RIGHT:
            self.x = self.x + (screen.get_width()/5)

    # Defect means shoot the thang
    def defect(self):
        # shoot bullet in straight line
        py.draw.line(screen, "cyan", py.Vector2(self.x, self.y), py.Vector2(screen.get_width(), self.y))

player1 = Player(50, screen.get_height() / 2, Direction.RIGHT)
player2 = Player(screen.get_width() - 50, screen.get_height() / 2, Direction.LEFT)
    
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    py.draw.circle(screen, "red", py.Vector2(player1.x, player1.y), 50.0, 25)
    py.draw.circle(screen, "cyan", py.Vector2(player2.x, player2.y), 50.0, 25)

    keys = py.key.get_pressed()
    if keys[py.K_d]:
        player1.defect()
    if keys[py.K_c]: 
        player1.coop() 
    if keys[py.K_1]:
        player2.defect()
    if keys[py.K_0]:
        player2.coop()

    # flip() the display to put your work on screen
    py.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
py.quit()