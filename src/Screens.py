import pygame
from src.SnakeBodyPartsControl import SnakeBodyPartsControl
from src.SnakeParts import SnakeParts
from src.Emotions import Emotions

class Screen:
  def __init__(self):
    '''
    Initialize the snake, emotion, and text display on playboard; also intialize other screens
    args: None
    return: None
    '''
    pygame.init()
    pygame.font.init()
    self.screenDimension = (700, 850)
    self.backgroundColor = (45, 115, 51)
    numInitialEmotion = 5
    self.surface = pygame.display.set_mode(self.screenDimension)
    self.windown_cap = pygame.display.set_caption("Snake game by tomatoes")
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill(self.backgroundColor)
    self.snake = SnakeBodyPartsControl()
    self.initialEmotions = pygame.sprite.Group()
    for i in range (numInitialEmotion):
      iniEmotions = Emotions.generateEmotions()
      iEmotions = Emotions(iniEmotions[0], iniEmotions[1])
      self.initialEmotions.add(iEmotions)
    self.speed = 0

  def exitScreen(self, imageFile=""):
    '''
    Calls the end screen (congrats/try again) after game over.
    args (str): Takes in the return from the score to display the right end screen.
    return (boolean): Returns a boolean for the controlor to call the start screen for button detection.
    '''
    image = pygame.image.load(imageFile)
    image = pygame.transform.smoothscale(image,     self.screenDimension)
    self.background.blit(image,(0,0))
    while True:
      self.surface.blit(self.background,(0,0))
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          highScoreFile = open("src/highScore.txt", "w")
          highScoreFile.write(str(0))
          highScoreFile.close()
          exit()
        mouth = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if mouth[1] > 550 and mouth[1] < 720 and mouth[0] > 150 and mouth[0] < 550:
            return True
          
  def startScreen(self):
    '''
    Genarates the start botton & start the game when user press it
    args: None
    return (boolean):  Returns a boolean for the controlor to call the start screen for botton detection
    '''
    image = pygame.image.load("assets/Screen/StartButton.png")
    image = pygame.transform.smoothscale(image, self.surface.get_size())
    self.background.blit(image,(0,0))
    while True:
      self.surface.blit(self.background,(0,0))
      pygame.display.flip()
      mouth = pygame.mouse.get_pos()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          highScoreFile = open("src/highScore.txt", "w")
          highScoreFile.write(str(0))
          highScoreFile.close()
          exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if mouth[1] > 300 and mouth[1] < 550:
            return True
  
  def playBoard(self, score=0):
    '''
    Initialize the play board by drawing the lines (walls), the score display, the snake, and the emotion
    args (str): Takes in the score and display it on the top of the board
    return: None
    '''
    self.background = pygame.Surface(self.surface.get_size())
    self.background = self.background.convert()
    self.background.fill(self.backgroundColor)
    whiteColor = (255, 255, 255)
    blackColor = (0, 0, 0)
    wallWidth = 5
    pygame.draw.rect(self.background, whiteColor, (0,0, 700, 100))
    scoreFont = pygame.font.SysFont("comic sans", 50)
    scoreLable = scoreFont.render("Current Score:" + str(score), 1, blackColor)
    pygame.draw.line(self.background, blackColor, (0, 100), (0, 850), wallWidth)
    pygame.draw.line(self.background, blackColor, (0, 850), (700, 850), wallWidth)
    pygame.draw.line(self.background, blackColor, (700, 850), (700, 100), wallWidth)
    pygame.draw.line(self.background, blackColor, (700, 100), (0, 100), wallWidth)
    self.initialSnake = pygame.sprite.RenderPlain(self.initialSnake)
    self.initialSnake.draw(self.background)
    initEmotions = pygame.sprite.RenderPlain(self.initialEmotions)
    initEmotions.draw(self.background)
    self.surface.blit(self.background,(0,0))
    self.surface.blit(scoreLable, (130, 25))
    pygame.display.flip()

  def drawSnake (self, input=None):
    '''
    Initialize the snake and make it move for play board; Also takes in the direction input from the user
    args (str): Takes in the user direction input & move the snake based on it
    return (boolean): Returns a state for the exit screen
    '''
    head = self.snake.snakeParts[0]
    self.blockSize = 50
    if input == None or input == head.inverse():
      input = head.direction
    status = "Alive"
    head.headDirectionControl(input, status)
    headRect = ()
    if head.direction == "Right":
      headRect = (head.rect[0] + self.blockSize, head.rect[1])
      if head.rect[0] + self.blockSize >= 700:
        status = "Dead"
    elif head.direction == "Left":
      headRect = (head.rect[0] - self.blockSize, head.rect[1])
      if head.rect[0] - self.blockSize < 0:
        status = "Dead"
    elif head.direction == "Up":
      headRect = (head.rect[0], head.rect[1] - self.blockSize)
      if head.rect[1] - self.blockSize < 100:
        status = "Dead"
    elif head.direction == "Down":
      headRect = (head.rect[0], head.rect[1] + self.blockSize)
      if head.rect[1] + self.blockSize >= 850:
        status = "Dead"
    for i in self.snake.snakeParts[1:]:
      if i.rect == headRect:
        status = "Dead"
        break
    if status == "Alive":
      self.snake.partsLocationControl()
      if head.direction == "Left":
        head.headLocationControl(head.rect[0] - self.blockSize, head.rect[1])
      if head.direction == "Right":
        head.headLocationControl(head.rect[0] + self.blockSize, head.rect[1])
      if head.direction == "Up":
        head.headLocationControl(head.rect[0], head.rect[1] - self.blockSize)
      if head.direction == "Down":
        head.headLocationControl(head.rect[0], head.rect[1] + self.blockSize)
    head.headDirectionControl(input, status)
    self.initialSnake = pygame.sprite.Group()
    for i in self.snake.snakeParts:
      self.initialSnake.add(i)
    if status == "Dead":
      return True

  def eating (self):
    '''
    Kill the emotion after it being eaten & keep track of the point gain
    args: None
    return (int): Return the total current points
    '''
    head = self.snake.snakeParts[0]
    points = 0
    for i in self.initialEmotions:
      if head.rect == i.rect:
        points = i.emotionEffects()
        if i.type == "Angry" and self.speed > -3:
          self.speed -= 1
        elif i.type == "Scared" and self.speed < 3:
          self.speed += 1
        break
    for i in range(points):
      lastSegment = self.snake.snakeParts[-1]
      newRect = ()
      if lastSegment.direction == "Right":
        newRect = (lastSegment.rect[0]-self.blockSize, lastSegment.rect[1])
      elif lastSegment.direction == "Left":
        newRect = (lastSegment.rect[0]+self.blockSize, lastSegment.rect[1])
      elif lastSegment.direction == "Up":
        newRect = (lastSegment.rect[0], lastSegment.rect[1]-self.blockSize)
      elif lastSegment.direction == "Down":
        newRect = (lastSegment.rect[0], lastSegment.rect[1]+self.blockSize)
      newBody = SnakeParts("assets/SnakeParts/SnakeBody.png", newRect, lastSegment.direction)
      self.snake.snakeParts.append(newBody)
    return points

  def newEmotions(self):
    '''
    Keep drawing emotions through out the game
    args: None
    return: None
    '''
    iniEmotions = Emotions.generateEmotions()
    iEmotions = Emotions(iniEmotions[0], iniEmotions[1])
    self.initialEmotions.add(iEmotions)