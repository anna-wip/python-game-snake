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
            self.head[0] += 1
         if self.direction == 'LEFT':
            self.head[0] -= 1
        if self.direction == 'UP':
            self.head[0] -= 1
        if self.direction == 'DOWN':
            self.head[0] += 1

class Food()
    def __init__(self):
        self.position = [random.randrange(1,72)*10, random.randrange(1,46)*10]
        self.spawn = true

#Initialising the game
snake = Snake()
food = Food()

gameSurface = pygame.display.setMode((500,250)
pygame.display.set_caption("Your Snake Game starts in the next few seconds...")
pygame.time.wait(1000)



