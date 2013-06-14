import pygame
from pygame.locals import *
from MyUtils import *

class Weapon:
    def __init__(self, char):
        self.char = char
        self.hrect = pygame.Rect(0, 0, 30, 60)
        self.vrect = pygame.Rect(0, 0, 60, 30)
        self.attack = 5

    def attack2(self, direc, enemies):
        if direc == 0:                                      #Right
            self.hrect.midleft = self.char.rect.midright
            rect = self.hrect
        elif direc == 1:                                    #Left
            self.hrect.midright = self.char.rect.midleft
            rect = self.hrect
        elif direc == 2:                                    #Down
            self.vrect.midtop = self.char.rect.midbottom
            rect = self.vrect
        elif direc == 3:                                    #Up
            self.vrect.midbottom = self.char.rect.midtop
            rect = self.vrect
        for en in enemies:
            if rect.colliderect(en.rect):
                en.rsound.play(3, 1)
                en.kill()
