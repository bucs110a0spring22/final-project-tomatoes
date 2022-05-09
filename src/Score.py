class Scores:
  def __init__(self):
    '''
    Initialize the score tracker and the highest score.
    args: None
    return: None
    '''
    self.scoreCount = 0
    highScoreFile = open("src/highScore.txt", "r")
    highScore = int(highScoreFile.read())
    highScoreFile.close()
    self.highestScore = highScore
    
  def finalScoreHighest(self):
    '''
    Keep track of the history highest score & compare with the current score
    args: None
    return (str): Returns the file path to the right end screen display
    '''
    if self.scoreCount > self.highestScore:
      highScoreFile = open("src/highScore.txt", "w")
      highScoreFile.write(str(self.scoreCount))
      highScoreFile.close()
      return "assets/Screen/Congratulations.png"
    if self.scoreCount <= self.highestScore:
      return "assets/Screen/TryAgain.png"
       