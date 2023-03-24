import time
import pygame
from pygame.locals import *

SIZE = 40

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.direction = "DOWN"
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.ps = parent_screen

    def draw(self):
        self.ps.fill((110, 110, 5))
        for i in range(self.length):
            self.ps.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def moveu(self):
        self.y -= 10
        self.draw()

    def moved(self):
        self.y += 10
        self.draw()
    
    def movel(self):
        self.x -= 10
        self.draw()

    def mover(self):
        self.x += 10
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
        self.surface.fill((110, 110, 5))  
        self.snake = Snake(self.surface, 6)
        self.snake.draw()

    def run(self): 
        running = True

        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_UP:
                        self.snake.direction = "UP"
                    if event.key == K_DOWN:
                        self.snake.direction = "DOWN"
                    if event.key == K_LEFT:
                        self.snake.direction = "LEFT"
                    if event.key == K_RIGHT:
                        self.snake.direction = "RIGHT"

                elif event.type == QUIT:
                    running = False   
        
            self.snake.step()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()