from src.SnakeParts import SnakeParts

class SnakeBodyPartsControl:
  def __init__(self):
    '''
    Initialize the position & status of the head and the body parts
    args: None
    return: None
    '''
    self.snakeParts = []
    desiredInitialHeadLocation = (350, 350)
    head = SnakeParts("assets/SnakeParts/SnakeHeadLeft.png", desiredInitialHeadLocation, "Left")
    self.snakeParts.append(head)
    self.block_size = 50
    for i in range(3):
      x = 350 + self.block_size * (i+1)
      body = SnakeParts("assets/SnakeParts/SnakeBody.png", (x,350), "Left")
      self.snakeParts.append(body)
    
  def partsLocationControl(self):
    '''
    Updates the heading of body parts when they're moved using the input
    args: None
    return: None
    '''
    for i in self.snakeParts[:0:-1]:
      i.rect = self.snakeParts[self.snakeParts.index(i)-1].rect