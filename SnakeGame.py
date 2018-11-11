
from pygame.locals import *
import pygame
import time
from random import randint

# Create Player class
class Player(pygame.sprite.Sprite):
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 1

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        pygame.sprite.Sprite.__init__(self)
        self.length = length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)

    def update(self):
        self.updateCount = self.updateCount + 1

        if self.updateCount > self.updateCountMax:

            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if self.direction == 0:
                self.x[0] += self.step
            if self.direction == 1:
                self.x[0] -= self.step 
            if self.direction == 2:
                self.y[0] -= self.step
            if self.direction == 3:
                self.y[0] += self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self, x, y):
        self.x = x*self.step
        self.y = y*self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

class App:

    # Create 800 x 600 grid
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(1)
        self.apple = Apple(5, 5)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption( ' SNAKE GAME!!!!!!')
        self._running = True

        # Scale snake image
        snake = pygame.image.load("Assets/hadto.jpg")
        snake = pygame.transform.scale(snake, (20, 20))

        # Scale apple image
        hadto = pygame.image.load("Assets/apple.png")
        hadto = pygame.transform.scale(hadto, (20, 20))
        
        self._image_surf = hadto.convert()
        self._apple_surf = snake.convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2, 9) * 44
                self.apple.y = randint(2, 9) * 44
                self.player.length += 1
                pygame.mixer.Sound("Assets/eatingSound.wav").play()
            if(self.player.length % 10 == 0):
                pygame.mixer.Sound("Assets/hiss.wav").play()
                

        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                self.dead()
            if(self.player.x[0] < 0 or self.player.x[0] > 800):
                self.dead()
            if(self.player.y[0] < 0 or self.player.y[0] > 600):
                self.dead()
        pass

    def start_screen(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.init()

        pygame.mixer.music.load("Assets/startMusic.mp3")
        pygame.mixer.music.play(-1)
        
        
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.font.init()
        titleFont = pygame.font.Font("Assets/titleFont.ttf", 200)
        subtitleFont = pygame.font.Font("Assets/subtitleFont.ttf", 40) 
            
        title = titleFont.render("SNAKE GAME!!!", False, (255, 20, 20))
        subtitle = subtitleFont.render("press F to continue...", False, (125, 255, 102))
        subtitleQ = subtitleFont.render("Q is for quitters", False, (125, 255, 102))
        
        pygame.display.set_caption('START')
        self._running = True

        background = pygame.image.load("Assets/titlescreen.jpg")
        background = pygame.transform.scale(background, (800,600)).convert()

        while(self._running):
            pygame.event.pump()
                        
            self._display_surf.blit(background, [0,0])
            self._display_surf.blit(title, [70, 150])
            self._display_surf.blit(subtitle, [250, 350])
            self._display_surf.blit(subtitleQ, [270, 400])
            pygame.display.flip()
            

            keys = pygame.key.get_pressed()

            if(keys[K_f]):
                self.instructions()
            if(keys[K_q]):
                self._running = False
    def instructions(self):
        pygame.mixer.music.load("Assets/instructionMusic.mp3")
        pygame.mixer.music.play(-1)
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        subtitleFont = pygame.font.Font("Assets/subtitleFont.ttf", 40)
        color = (255, 46, 0) 

        instructions = subtitleFont.render("Arrow Keys to move,", False, color)
        objective = subtitleFont.render("Eat all the apples,", False, color)
        quitters = subtitleFont.render("Q to quit,", False, color)
        subtitle = subtitleFont.render("press F to continue...", False, color)
        
        pygame.display.set_caption('INSTRUCTIONS')
        self._running = True

        background = pygame.image.load("Assets/grass.jpg")
        background = pygame.transform.scale(background, (800,600)).convert()

        while(self._running):
            pygame.event.pump()
                        
            self._display_surf.blit(background, [0,0])
            self._display_surf.blit(instructions, [100, 150])
            self._display_surf.blit(objective, [100, 200])
            self._display_surf.blit(quitters, [100, 300])
            self._display_surf.blit(subtitle, [100, 400])
            
            pygame.display.flip()
            

            keys = pygame.key.get_pressed()

            if(keys[K_f]):
                self.on_execute()
            if(keys[K_q]):
                self._running = False
                
    def dead(self):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("Assets/youDied.wav").play(0)
        subtitleFont = pygame.font.Font("Assets/subtitleFont.ttf", 60)
        color = (170, 170, 170)

        score = subtitleFont.render("Your Score: " + str(self.player.length), False, color)
        quitter = subtitleFont.render("Press Q to quit", False, color)

        background = pygame.image.load("Assets/youDied.jpg")
        background = pygame.transform.scale(background, [800, 600])

        while (self._running):
            pygame.event.pump()
            
            self._display_surf.blit(background.convert(), (0, 0))
            self._display_surf.blit(score, (250, 430))
            self._display_surf.blit(quitter, (250, 460))
            pygame.display.flip()

            keys = pygame.key.get_pressed()

            if(keys[K_q]):
                self._running = False
                
    def on_render(self):
        grass = pygame.image.load("Assets/grass.jpg")
        grass = pygame.transform.scale(grass, (800,600))
        self._display_surf.blit(grass.convert(), [0, 0])

        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        pygame.mixer.init()
        pygame.font.init()
        pygame.mixer.music.load("Assets/gameMusic.mp3")
        pygame.mixer.music.play(-1)
        
        if self.on_init() == False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if(keys[K_RIGHT]):
                self.player.moveRight()

            if(keys[K_LEFT]):
                self.player.moveLeft()

            if(keys[K_UP]):
                self.player.moveUp()

            if(keys[K_DOWN]):
                self.player.moveDown()

            if(keys[K_q]):
                self._running = False

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.start_screen()
