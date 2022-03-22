import pygame
#import your controller

mylist = [int(input("Please enter a number")), int(input("Please enter the same number again")), int(input("Please enter the same number again")), int(input("Please enter the same number again"))]
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
mylist[0],mylist[3] = mylist[3], mylist[0]

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
