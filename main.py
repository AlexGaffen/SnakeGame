import pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.ps = parent_screen

    def draw(self):
        self.ps.fill((110, 110, 5))
        self.ps.blit(self.block, (self.x, self.y))
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

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill((110, 110, 5))  
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self): 
        running = True

        
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                    if event.key == K_UP:
                        self.snake.moveu()
                    if event.key == K_DOWN:
                        self.snake.moved()
                    if event.key == K_LEFT:
                        self.snake.movel()
                    if event.key == K_RIGHT:
                        self.snake.mover()

                elif event.type == QUIT:
                    running = False   

if __name__ == "__main__":
    game = Game()
    game.run()