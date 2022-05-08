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
        input = None
        pygame.time.wait(500)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
              input = "Right"
            if event.key == pygame.K_LEFT:
              input = "Left"
            if event.key == pygame.K_DOWN:
              input = "Down"
            if event.key == pygame.K_UP:
              input = "Up"
          if event.type == pygame.QUIT:
            exit()
        if self.screen.playBoard(input):
          self.state = "GAME OVER"
      elif(self.state == "GAME OVER"):
        if self.screen.exitScreen():
          exit()
      elif (self.state == "GAME ON"):
        if self.screen.startScreen():
          self.state = "GAME"