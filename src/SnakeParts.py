import pygame

class SnakeParts(pygame.sprite.Sprite):
  def __init__(self, image, location, direction):
    '''
    Initialize the snake
    args (str, tuple, str): Takes in the image's file path, location, and direction for both body parts & head
    return: None
    '''
    pygame.sprite.Sprite.__init__(self)
    self.blockDimension = (50,50)
    self.image = pygame.image.load(image)
    self.image = pygame.transform.smoothscale(self.image, self.blockDimension)
    self.rect = location
    self.direction = direction

  def headDirectionControl(self, direction, status=""):
    '''
    Updates the heading and status of head when game is on using the input, then use them to determine the correct image file to use
    args (str): Takes in the direction & status of the head
    return: None
    '''
    self.direction = direction
    haha = None
    if status == "Alive":
      if direction == "Right":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadRight.png")
      if direction == "Left":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadLeft.png")
      if direction == "Up":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadUp.png")
      if direction == "Down":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDown.png")
    else:
      if direction == "Right":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadRight.png")
      if direction == "Left":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadLeft.png")
      if direction == "Up":
        haha = pygame.image.load("assets/SnakeParts/SnakeHeadDeadUp.png")
      if direction == "Down":
        haha = pygame.image.load("assets/Snakeparts/SnakeHeadDeadDown.png")
    self.image = pygame.transform.smoothscale(haha, self.blockDimension)
    
  def headLocationControl(self, x=0, y=0):
    '''
    Updates the coordinates of head when they're moved using the input
    args (int): Takes in the x & y coordinates of the snake
    return: None
    '''
    self.rect = (x,y)
    
  def inverse (self):
    '''
    Takes the current direction of the snake & stops the user from input the opposite direction directly
    args: None
    return (str): Returns the direction that the user can't move toward.
    '''
    if self.direction == "Right":
      return "Left"
    if self.direction == "Left":
      return "Right"
    if self.direction == "Up":
      return "Down"
    if self.direction == "Down":
      return "Up"