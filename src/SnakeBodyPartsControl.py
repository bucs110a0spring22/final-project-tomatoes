import pygame 
from SnakeParts import SnakeParts
from Screens import Screen

class SnakeBodyPartsControl:
  def __init__(self):
    # Initialize the position & status of the body parts
    self.snakeParts = []
    head = SnakeParts("assets/SnakeHead.png", (350,350), "Right")
    self.snakeParts.append(head)
    block_size = 50
    for i in range(3):
      x = 350 + block_size * (i+1)
      body = SnakeParts("assets/SnakeBody.png", (x,350), "Right")
      self.snakeParts.append(body)
    
  def partsLocationControl(self, index):
    # Updates the heading of body parts when they're moved using the input
    for i in self.snakeParts[:0:-1]:
      i.rect = self.snakeParts[self.snakeParts.index(i)-1].rect
      