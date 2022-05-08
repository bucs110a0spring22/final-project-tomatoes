import pygame
from pygame.locals import * #Can we not use this?
from src.SnakeBodyPartsControl import SnakeBodyPartsControl
from src.SnakeParts import SnakeParts
from src.Emotions import Emotions
# from Score import Scores 

class Screen:
  def __init__(self):
    # Initialize the Screens
    pygame.init()
    pygame.font.init()
    self.surface = pygame.display.set_mode((700,850))
    # y come first instead of x
    self.windown_cap = pygame.display.set_caption("Snake game by tomatoes")
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill((45, 115, 51))
    #Find a pic of this color & resize it to 750x750 so there's place to display score while play   
    self.snake = SnakeBodyPartsControl()

  def exitScreen(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            return True
          
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
        if event.type == QUIT:
          exit()
        if event.type == MOUSEBUTTONDOWN:
          if mouth[1] > 300 and mouth[1] < 550:
            return True
  
  def playBoard(self, input = None):
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill((45, 115, 51))
    pygame.draw.rect(self.background, (255, 255, 255), (0,0, 700, 100))
    scoreFont = pygame.font.SysFont("comic sans", 50)
    scoreLable = scoreFont.render("Current Score:", 1, (0, 0, 0))
    pygame.draw.line(self.background,(0, 0, 0), (0, 100), (0, 850), 5)
    pygame.draw.line(self.background,(0, 0, 0), (0, 850), (700, 850), 5)
    pygame.draw.line(self.background,(0, 0, 0), (700, 850), (700, 100), 5)
    pygame.draw.line(self.background,(0, 0, 0), (700, 100), (0, 100), 5)
    head = self.snake.snakeParts[0]
    if input == None or input == head.inverse():
      input = head.direction
    status = "Alive"
    head.headDirectionControl(input, status)
    if head.direction == "Left":
      if head.rect[0] - 50 < 0:
        status = "Dead"
    if head.direction == "Right":
      if head.rect[0] + 50 >= 700:
        status = "Dead"
    if head.direction == "Up":
      if head.rect[1] - 50 < 100:
        status = "Dead"
    if head.direction == "Down":
      if head.rect[1] + 50 >=850:
        status = "Dead"
    if status == "Alive":
      self.snake.partsLocationControl()
      if head.direction == "Left":
        head.headLocationControl(head.rect[0] - 50, head.rect[1])
      if head.direction == "Right":
        head.headLocationControl(head.rect[0] + 50, head.rect[1])
      if head.direction == "Up":
        head.headLocationControl(head.rect[0], head.rect[1] - 50)
      if head.direction == "Down":
        head.headLocationControl(head.rect[0], head.rect[1] + 50)
    head.headDirectionControl(input, status)
    for i in self.snake.snakeParts[1:]:
      if i.rect == head.rect:
        status = "Dead"
    head.headDirectionControl(input, status)
    initialSnake = pygame.sprite.Group()
    for i in self.snake.snakeParts:
      initialSnake.add(i)
    initialSnake = pygame.sprite.RenderPlain(initialSnake)
    initialSnake.draw(self.background)
    # initialEmotions = pygame.sprite.Group()
    self.surface.blit(self.background,(0,0))
    self.surface.blit(scoreLable, (130, 25))
    pygame.display.flip()
    if status == "Dead":
      pygame.time.wait(1000)
      return True