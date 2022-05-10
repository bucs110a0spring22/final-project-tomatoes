import pygame 
from src.Screens import Screen
from src.Score import Scores

class Controller:
  def __init__(self):
    ''' 
    Initialize pygame, the state of the game, the font, and the screen.
    args: None
    return: None
    '''
    pygame.init()
    pygame.font.init()
    self.state = "GAME ON"
    self.screen = Screen()
    self.score = Scores()
  
  def mainloop(self):
    '''
    Controls the time that the frames refresh; takes the direction input from the user; and call corresponding screen based on the status of the game.
    args: None
    return: None
    '''
    timeCount = 0
    while True:
      if(self.state == "GAME"):
        input = None
        waitTime = 500
        pygame.time.wait(waitTime + self.screen.speed * 200)
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
            highScoreFile = open("src/highScore.txt", "w")
            highScoreFile.write(str(0))
            highScoreFile.close()
            exit()
        if self.screen.drawSnake(input):
          self.state = "GAME OVER"
        mango = self.screen.eating()
        self.score.scoreCount += mango
        if timeCount % 7 == 0:
          self.screen.newEmotions()
        self.screen.playBoard(self.score.scoreCount)
        timeCount += 1
      elif(self.state == "GAME OVER"):
        pygame.time.wait(waitTime * 2)
        endScreen = self.score.finalScoreHighest()
        if self.screen.exitScreen(endScreen):
          return True
      elif (self.state == "GAME ON"):
        if self.screen.startScreen():
          self.state = "GAME"