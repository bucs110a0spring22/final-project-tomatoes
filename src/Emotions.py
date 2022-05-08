import pygame
import random 
from pygame.locals import *

class Emotions(pygame.sprite.Sprite):
  def __init__(self, type, location):
    # Initialize emotions
    self.rec = location
    self.type = type
    if type == "Happy":
      self.image = pygame.image.load("assets/Happy.png")
    if type == "Sad":
      self.image = pygame.image.load("assets/Sad.png")
    if type == "Angry":
      self.image = pygame.image.load("assets/Angry.png")
    if type == "Scared":
      self.image = pygame.image.load("assets/Scared.png")
    if type == "Excited":
      self.image = pygame.image.load("assets/Excited.png")
    
  @staticmethod #Allow the method to be called even before the object is made
  def generateEmotions ():
    # Randomly generate emotion types & coordinantes for the play board 
    typePossible = ["Happy", "Sad", "Angry", "Scared", "Excited"]
    type = random.choice(typePossible)
    x = random.randrange(0,701,50)
    y = random.randrange(100,801,50)
    location = (x,y)
    return type, location

  def emotionEffects(self):
    # Links the effects of emotions to the actual emotion itself.
    if self.type == "Sad":
      return -1
    elif self.type == "Excited":
      return 4
    else:
      return 1

  def emotionKilled(self, emotionLess):
    # Update the counters when the head run into an Emotions
    if self.type == "Happy":
      emotionLess[0].append(1)
    if self.type == "Sad":
      emotionLess[1].append(1)
    if self.type == "Angry":
      emotionLess[2].append(1)
    if self.type == "Scared":
      emotionLess[3].append(1)
    if self.type == "Excited":
      emotionLess[4].append(1)
    self.kill()
    
      