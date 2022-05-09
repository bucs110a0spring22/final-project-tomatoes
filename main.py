import pygame
from src.Controller import Controller

def main():
  while True:
    control = Controller()
    control.mainloop()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        highScoreFile = open("src/highScore.txt", "w")
        highScoreFile.write(str(0))
        highScoreFile.close()
        exit()


if __name__ == "__main__":
  main()