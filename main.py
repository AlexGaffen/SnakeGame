import time
import time
import pygame
import random
from pygame.locals import *

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.ps = parent_screen
        self.x = SIZE*random.randint(0,24)
        self.y = SIZE*random.randint(0,19)

    def draw(self):
        self.ps.blit(self.image, (self.x, self.y))
        pygame.display.flip()   

    def move(self):
        self.x = SIZE*random.randint(0,24)
        self.y = SIZE*random.randint(0,19)


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.direction = "DOWN"
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.direction = "DOWN"
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.ps = parent_screen

    def draw(self):
        self.ps.fill((110, 110, 5))
        for i in range(self.length):
            self.ps.blit(self.block, (self.x[i], self.y[i]))
        for i in range(self.length):
            self.ps.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def step(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "UP":
            self.y[0] -= SIZE
        if self.direction == "DOWN":
            self.y[0] += SIZE
        if self.direction == "LEFT":
            self.x[0] -= SIZE
        if self.direction == "RIGHT":
            self.x[0] += SIZE

        self.draw()        


    def step(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "UP":
            self.y[0] -= SIZE
        if self.direction == "DOWN":
            self.y[0] += SIZE
        if self.direction == "LEFT":
            self.x[0] -= SIZE
        if self.direction == "RIGHT":
            self.x[0] += SIZE

        self.draw()        


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,800))
        self.surface = pygame.display.set_mode((1000,800))
        self.surface.fill((110, 110, 5))  
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.step()
        self.apple.draw()
        self.score()
        pygame.display.flip()

    def collision(self):
        return self.snake.x[0] == self.apple.x and self.snake.y[0] == self.apple.y
    
    def scollision(self):
        if self.snake.length > 1: 
            for i in range(1,self.snake.length):
                if self.snake.x[0] == self.snake.x[i] and self.snake.y[0] == self.snake.y[i]:
                    return True
        return False   
    
    def score(self):
        font = pygame.font.SysFont('arial',40,True)
        score = font.render(f"Score: {self.snake.length}", True, (0,0,255))
        self.surface.blit(score, (800, 10))

    def run(self): 
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_UP:
                        self.snake.direction = "UP"
                        self.snake.direction = "UP"
                    if event.key == K_DOWN:
                        self.snake.direction = "DOWN"
                        self.snake.direction = "DOWN"
                    if event.key == K_LEFT:
                        self.snake.direction = "LEFT"
                        self.snake.direction = "LEFT"
                    if event.key == K_RIGHT:
                        self.snake.direction = "RIGHT"
                        self.snake.direction = "RIGHT"

                elif event.type == QUIT:
                    running = False   

            if self.collision():
                self.snake.x.append(self.snake.x[self.snake.length-1])
                self.snake.y.append(self.snake.y[self.snake.length-1])
                self.snake.length += 1     
                self.apple.move()   

            elif self.scollision():
                running = False        

            self.play()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()