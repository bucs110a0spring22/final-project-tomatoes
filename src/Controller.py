import pygame 
# import time
# from Emotions import Emotions
from src.Screens import Screen

class Controller:
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.font.init()
    # self.emotion = pygame.sprite.Group()
    #  num_emotion = 2
    # self.all_sprites = pygame.sprite.Group((self.snake,) + tuple(self.emotion))
    self.state = "GAME ON"
    self.screen = Screen()
  
  def mainloop(self):
    #select state loop
     while True:
      if(self.state == "GAME"):
        if self.screen.playBoard():
          self.state = "GAME OVER"
      elif(self.state == "GAME OVER"):
        if self.screen.exitScreen():
          print("sleppy")
      elif (self.state == "GAME ON"):
        if self.screen.startScreen():
          self.state = "GAME"
      
  # def userInput(self):
    