import pygame 
from src.SnakeParts import SnakeParts

class SnakeBodyPartsControl:
  def __init__(self):
    # Initialize the position & status of the body parts
    self.snakeParts = []
    head = SnakeParts("assets/SnakeParts/SnakeHeadLeft.png", (350,350), "Left")
    self.snakeParts.append(head)
    block_size = 50
    for i in range(3):
      x = 350 + block_size * (i+1)
      body = SnakeParts("assets/SnakeParts/SnakeBody.png", (x,350), "Left")
      self.snakeParts.append(body)
    
  def partsLocationControl(self):
    # Updates the heading of body parts when they're moved using the input
    for i in self.snakeParts[:0:-1]:
      i.rect = self.snakeParts[self.snakeParts.index(i)-1].rect