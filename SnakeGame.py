
import pygame
from pygame.locals import *

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
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption( ' SNAKE GAME!!!!!!')
        self._running = True
        self._image_surf = pygame.image.load("Assets/grass.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        
