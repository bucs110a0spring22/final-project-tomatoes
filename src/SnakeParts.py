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
        pygame.image.load("SnakeHeadRight")
      if direction == "Left":
        pygame.image.load("SnakeHeadLeft")
      if direction == "Up":
        pygame.image.load("SnakeHeadUp")
      if direction == "Down":
        pygame.image.load("SnakeHeadDown")
    else:
      if direction == "Right":
        pygame.image.load("SnakeHeadDeadRight")
      if direction == "Left":
        pygame.image.load("SnakeHeadDeadLeft")
      if direction == "Up":
        pygame.image.load("SnakeHeadDeadUp")
      if direction == "Down":
        pygame.image.load("SnakeHeadDeadDown")
    
  def headLocationControl(self, x=0, y=0):
    # Updates the coordinates of head when they're moved using the input
    self.rect[0] = x
    self.rect[1] = y

  def tailDirectionControl(self, direction=""):
    # Update the direction of the tail & rotate the image accordingly
    self.direction = direction
    if direction=="Right":
      pygame.image.load("TailRight")
    if direction=="Left":
      pygame.image.load("TailLeft")
    if direction=="Up":
      pygame.image.load("TailUp")
    if direction=="Down":
      pygame.image.load("TailDown")