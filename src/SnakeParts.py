import pygame
from SankeBodyParts import SnakeBodyPartsControl
from pygame.locals import *

class SnakeParts(pygame.sprite.Sprite):
  def __init__(self, image, location, direction):
    # Initialize the snake
    self.image = pygame.image.load("Head")
    self.rect = location
    self.direction = direction

  def headDirectionControl(self, direction="", status=""):
    # Updates the heading & status of head when game is on using the input
    self.direction = direction
    if status == "Alive":
      if direction == "Right":
        pygame.image.load("assets/SnakeHeadRight")
      if direction == "Left":
        pygame.image.load("assets/SnakeHeadLeft")
      if direction == "Up":
        pygame.image.load("assets/SnakeHeadUp")
      if direction == "Down":
        pygame.image.load("assets/SnakeHeadDown")
    else:
      if direction == "Right":
        pygame.image.load("assets/SnakeHeadDeadRight")
      if direction == "Left":
        pygame.image.load("assets/SnakeHeadDeadLeft")
      if direction == "Up":
        pygame.image.load("assets/SnakeHeadDeadUp")
      if direction == "Down":
        pygame.image.load("assets/SnakeHeadDeadDown")
    
  def headLocationControl(self, x=0, y=0):
    # Updates the coordinates of head when they're moved using the input
    self.rect[0] = x
    self.rect[1] = y
