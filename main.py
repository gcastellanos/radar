import pygame
from pygame.locals import *
from worldClass import *
from Events import *

def main():
    w = world()
    w.eventloop()
    print(" press enter to exit")
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_RETURN:
                return

if __name__ ==  "__main__":
    main()
    pygame.quit()
