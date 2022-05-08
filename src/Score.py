from Emotions import Emotions

class Scores:
  def __init__(self):
    self.scoreCount = 0
    self.highestScore = 0
    
  def updateScores(self, type=None):
    # Keep track of the score while the player is playing the game (maybe a small screen displays the current score on left/right upper corner)
    if type == "Happy":
      self.score += 1
    if type == "Sad":
      self.score -= 1
    if type == "Angry":
      self.score += 1
    if type == "Scared":
      self.score += 1
    if type == "Excited":
      self.score += 4
    
  def finalScoreHighest(self):
    # Keep track of the history highest score (only saves the highest) & compare with the curren score
    if self.scoreCount > self.highestScore:
      self.highestScore = self.scoreCount
      return "assets/Congradulation.png"
    if self.scoreCount < self.highestScore:
      return "assets/TryAgain.png"
       