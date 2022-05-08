import pygame
from pygame.locals import *

class SnakeParts(pygame.sprite.Sprite):
  def __init__(self, image, location, direction):
    # Initialize the snake
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image)
    self.image = pygame.transform.smoothscale(self.image, (50,50))
    self.rect = location
    self.direction = direction

  def headDirectionControl(self, direction, status=""):
    # Updates the heading & status of head when game is on using the input
    self.direction = direction
    haha = None
    if status == "Alive":
      if direction == "Right":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadRight.png")
      if direction == "Left":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadLeft.png")
      if direction == "Up":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadUp.png")
      if direction == "Down":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDown.png")
    else:
      if direction == "Right":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadRight.png")
      if direction == "Left":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadLeft.png")
      if direction == "Up":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadUp.png")
      if direction == "Down":
        haha = pygame.image.load("assets/Snakeparts/SnakeHeadDeadDown.png")
    self.image = pygame.transform.smoothscale(haha, (50,50))
    
  def headLocationControl(self, x=0, y=0):
    # Updates the coordinates of head when they're moved using the input
    self.rect = (x,y)
  def inverse (self):
    if self.direction == "Right":
      return "Left"
    if self.direction == "Left":
      return "Right"
    if self.direction == "Up":
      return "Down"
    if self.direction == "Down":
      return "Up"