#Einsendeaufgabe 3 - Data Science - Anna Weigand - Python game SNAKE

import pygame
import sys
import time
import random

#Initialising the game
pygame.init()

#Game Surface
# each patch is 10 x 10 px -> 70x35 patches
gameSurface = pygame.display.set_mode((700,350))
pygame.display.set_caption("Python Snake Game")
pygame.time.wait(1000)

#Colors
black = pygame.Color(0,0,0)#Background
white = pygame.Color(255,255,255)#Score
green = pygame.Color(173,255,47)#Snake
orange = pygame.Color(255,165,0)#Food
red = pygame.Color(255,64,64)#GameOver

#FPS Controller
fpsController = pygame.time.Clock()

#Variables and directions
class Snake:
    def __init__(self):
        self.body = [[40,50],[30,50],[20,50]]
        self.position = [50, 50]
        self.direction = "RIGHT"
        self.score = 0

    def changeDirection(self, dir):
        if dir == 'RIGHT' and not self.direction == 'LEFT':
            self.direction = 'RIGHT'
        if dir == 'LEFT' and not self.direction == 'RIGHT':
            self.direction = 'LEFT'
        if dir == 'UP' and not self.direction == 'DOWN':
            self.direction = 'UP'
        if dir == 'DOWN' and not self.direction == 'UP':
            self.direction = 'DOWN'

    def move(self,food):
        if self.direction == 'RIGHT':
            mv = [10,0]
        if self.direction == 'LEFT':
            mv = [-10,0]
        if self.direction == 'UP':
            mv = [0,-10]
        if self.direction == 'DOWN':
            mv = [0,10]
        # change position according to mv
        # itemwise addition of two lists
        self.position = [self.position[i] + mv[i] for i in range(len(self.position))]

        # check if out of bounds
        w,h = pygame.display.get_surface().get_size()
        if self.position[0]<0 or self.position[0]>= w:
            gameOver(self)
        if self.position[1]<0 or self.position[1]>= h:
            gameOver(self)
        # check if eating myself
        if self.position in self.body:
            gameOver(self)

        # check if snake found food
        if self.position == food.position:
            # if yes: grow (add new position to current body)
            self.body = [self.position] + self.body
            # increase score
            self.score += 1
            # regrow food
            food.regrow()
            # if food was generated within existing snake, regrow
            while food.position in self.body:
                food.regrow()
                # TODO check if any fields possible at all!!
        else:
            # ... just move
            # append body except last element to self position as new body
            self.body = [self.position] + self.body[:len(self.body)-1]


class Food:
    def __init__(self):
        # get random position from display size in 10s of pxls
        self.regrow()

    def regrow(self):
        # get random position from display size in 10s of pxls
        w,h = pygame.display.get_surface().get_size()
        self.position = [random.randrange(0, (w / 10)-1)*10,
                         random.randrange(0, (h / 10)-1)*10]

def showScore(snake):
    scoreFont = pygame.font.SysFont('arial',24)
    scoreSurf = scoreFont.render('Score: {0}'.format(snake.score), True, white)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (80,10)

    gameSurface.blit(scoreSurf, scoreRect)

#Game Over
def gameOver(snake):
    myFont = pygame.font.SysFont('arial', 30)
    gameOverSurf = myFont.render(
                    "Snake Game | Your score: "+str(snake.score)+" | GAME OVER",
                    True, red)
    gameOverRect = gameOverSurf.get_rect()
    w,h = pygame.display.get_surface().get_size()
    gameOverRect.midtop = (w/2, h/2)
    gameSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# initialize snake and food:
sn = Snake()
fd = Food()

#Game Start
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver(sn)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sn.changeDirection("RIGHT")
            if event.key == pygame.K_LEFT:
                sn.changeDirection("LEFT")
            if event.key == pygame.K_UP:
                sn.changeDirection("UP")
            if event.key == pygame.K_DOWN:
                sn.changeDirection("DOWN")
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    sn.move(fd)

    # clear screen
    gameSurface.fill(black)
    # draw snake
    for position in sn.body:
        pygame.draw.rect(gameSurface,green,
                         pygame.Rect(position[0],position[1],10,10))
    # draw food
    pygame.draw.rect(gameSurface,orange,
                     pygame.Rect(fd.position[0],fd.position[1],10,10))

    #Show Score
    showScore(sn)
    pygame.display.flip()
    fpsController.tick(10)
