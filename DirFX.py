import pygame
from RadarSound import *
from MyUtils import *

class DirFX(pygame.sprite.Sprite):
    def __init__(self, loc, sounds, chan, smanager):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, 1, 1)
        self.rect.center = loc
        self.rsound = RadarSound(sounds, chan)
        self.smanager = smanager

    def die(self):
        self.smanager.returnChan(self.rsound.cid)
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

    def proximity(self, char):
        direc = getDirection(char.rect.center, self.rect.center)
        dist = getDistance(char.rect.center, self.rect.center)
        self.rsound.updateBools()
        for i in range(7):
            if char.circles[i].collideRect(self.rect):
                if isLeft(direc):
                    x = 2
                    n = 0
                elif isRight(direc):
                    x = 2 
                    n = 1
                elif isUp(direc):
                    x = 0 
                    n = 2
                else:
                    x = 1 
                    n = 3
                if not self.rsound.isBusy():
                    self.rsound.dirPlay(x, n, 2 ** (7 - i))
                return
        self.die()
