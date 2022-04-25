import pygame
from pygame.locals import * #Can we not use this?

class Screen:
  def __init__(self):
    # Initialize the Screens
    surface = pygame.display.set_mode((750,850), 0, 32)
    windown_cap = pygame.display.set_caption("Snake game by tomatoes")
    surface.fill((45, 115, 51))
    #Find a pic of this color & resize it to 750x750 so there's place to display score while play   
    running = True

  def exitScreen(self):
    while running:
      for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
          running = False
        elif event.type == QUIT: 
          running = FALSE
          
  def startScreen(self):
    # Genarates a start bottom in the middle and start the game when user press it.
    pygame.image.load("StartButton.png").convert()
    surface.blit(x,y)
  
  def playBoard(self):
    # Set up the playing board
    
  def finalScreenScores(self,final_score):
    # Display the total emotion eaten
    pygame.image.load("Congrats/Try it agian").convert()
    pic_x = 
    pic_y = 
    surface.blit(x,y)
     

pygame.display.update()