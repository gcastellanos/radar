import pygame, math
from pygame.locals import *
from MyUtils import *

class landmarks(pygame.sprite.Sprite):
    def __init__(self, dim, location, kill_dist):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(location, dim)
        self.image = pygame.Surface(dim)
        self.image.fill((200, 100 , 50))
        self.kill_dist = kill_dist

    def update(self, char):
        if getDistance(self.rect.center, char.rect.center) >= self.kill_dist:
            self.kill()

    def scroll(self, tup):
        if tup[1] == 3:
            self.rect = self.rect.move(0, tup[0])
        elif tup[1] == 2:
            self.rect = self.rect.move(0, -tup[0])
        elif tup[1] == 1:
            self.rect = self.rect.move(tup[0], 0)
        elif tup[1] == 0:
            self.rect = self.rect.move(-tup[0], 0)
        elif tup[1] == 4:
            self.rect = self.rect.move(-tup[0] * math.cos(math.radians(135)), tup[0] * math.sin(math.radians(135)))
        elif tup[1] == 5:
            self.rect = self.rect.move(tup[0] * math.cos(math.radians(135)), tup[0] * math.sin(math.radians(135)))
        elif tup[1] == 6:
            self.rect = self.rect.move(-tup[0] * math.cos(math.radians(135)), -tup[0] * math.sin(math.radians(135)))
        elif tup[1] == 7:
            self.rect = self.rect.move(tup[0] * math.cos(math.radians(135)), -tup[0] * math.sin(math.radians(135)))
