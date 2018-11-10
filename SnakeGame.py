
from pygame.locals import *
import pygame

# Create Player class
class Player:
    x = 10
    y = 10
    speed = 1

    # Defining movement direction with
    # grid origin in the topleft corner
    def moveRight(self):
        self.x += self.speed

    def moveLeft(self):
        self.x -= self.speed

    def moveUp(self):
        self.y -= self.speed

    def moveDown(self):
        self.y += self.speed

class App:

    # Create 800 x 600 grid
    windowWidth = 800
    windowHeight = 600

    def _init_(self):
        self._running = True

    def on_init(self):
        pygame.init
        
