#Einsendeaufgabe 3 - Data Science - Anna Weigand - Python game SNAKE

import pygame
import sys
import time
import random

#Colors
black = pygame.Color(0,0,0)#Background
white = pygame.Color(255,255,255)#Score
green = pygame.Color(173,255,47)#Snake
orange = pygame.Color(255,165,0)#Food
red = pygame.Color(255,64,64)#GameOver

#Variables and directions
class Snake()
    def __init__(self):
        self.body = [[40,50],[30,50],[20,50]]
        self.position = [50]
        self.direction = "RIGHT"
        
    def changeDirection (self,dir):
        if changeTo == 'RIGHT' and not direction == 'LEFT':
            direction = 'RIGHT'
        if changeTo == 'LEFT' and not direction == 'RIGHT':
            direction = 'LEFT'
        if changeTo == 'UP' and not direction == 'DOWN':
            direction = 'UP'
        if changeTo == 'DOWN' and not direction == 'UP':
            direction = 'DOWN'
    
    def move(self,foodPosition):
        if self.direction == 'RIGHT':
            self.position += 10
         if self.direction == 'LEFT':
            self.position -= 10
        if self.direction == 'UP':
            self.position -= 10
        if self.direction == 'DOWN':
            self.position += 10

class Food()
    def __init__(self):
        self.position = [random.randrange(1,50)*10, random.randrange(1,25)*10]
        self.spawn = true

#FPS Controller
fpsController = pygame.time.clock()

#Score
score = 0

#Initialising the game
snake = Snake()
food = Food()

gameSurface = pygame.display.setMode((500,250)
gameSurface.fill(black)
pygame.display.set_caption("Your Snake Game starts in the next few seconds...")
pygame.time.wait(1000)

#Score
def showScore(choice=1)
    scoreFont = pygame.font.SysFont('arial',24)
    scoreSurf = scoreFont.render('Score:{0}'.format(score), True, white)
    scoreRect = scoreSurf.get_rect()
    if choice ==1:
        scoreRect.midtop = (80,10)
    else
        scoreRect.midtop = (360,150)

    gameSurface.blit(scoreSurf, scoreRect)

#Game Over
def gameOver():
    pygame.display.setCaption("Snake Game | Your score: "+str(score)+" | GAME OVER)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#Game Start
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirection("RIGHT")
            if event.key == pygame.K_LEFT:
                snake.changeDirection("LEFT")
            if event.key == pygame.K_UP:
                snake.changeDirection("UP")
            if event.key == pygame.K_DOWN:
                snake.changeDirection("DOWN")
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

foodPosition = foodSpawn()
    if snake.move(foodPosition) == 1:
        score +=1
        foodSpawn = False
    else snakeBody.pop

gameSurface.fill(black)
    for position in snakeBody:
        pygame.draw.rect(gameSurface,green,pygame.Rect(snakePosition[0],snakePosition[1],10,10))

pygame.draw.rect(gameSurface,orange,pygame.Rect(foodPosition[0],foodPosition[1],10,10))

#Show Score
showScore()
pygame.display.flip()
fpsController.tick(1)


