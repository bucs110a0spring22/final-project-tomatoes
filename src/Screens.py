import pygame
from pygame.locals import * #Can we not use this?
# from Emotions import Emotions
# from Score import Scores 

class Screen:
  def __init__(self):
    # Initialize the Screens
    pygame.init()
    self.surface = pygame.display.set_mode((700,850))
    # y come first instead of x
    self.windown_cap = pygame.display.set_caption("Snake game by tomatoes")
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill((45, 115, 51))
    #Find a pic of this color & resize it to 750x750 so there's place to display score while play   
    self.running = True

  def exitScreen(self):
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
          return True
        elif event.type == pygame.QUIT: 
          exit()
          
  def startScreen(self):
    # Genarates a start bottom in the middle and start the game when user press it.
    image = pygame.image.load("assets/Screen/StartButton.png")
    image = pygame.transform.smoothscale(image, self.surface.get_size())
    self.background.blit(image,(0,0))
    while True:
      self.surface.blit(self.background,(0,0))
      pygame.display.flip()
      mouth = pygame.mouse.get_pos()
      for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
          if mouth[1] > 300 and mouth[1] < 550:
            return True
  
  def playBoard(self, input = None):
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill((45, 115, 51))
    self.surface.blit(self.background,(0,0))
    pygame.display.flip()
    return True