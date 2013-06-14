import pygame
from pygame.locals import *
from MyUtils import *


class Hitboxes(pygame.sprite.Sprite):
    def __init__(self, rect, time, type, atk, kb):
        pygame.sprite.Sprite.__init__(self)
        self.rect = rect
        self.timer = 0
        self.maxtime = time
        self.type = type
        self.attack = atk
        self.kb = kb
        
    def update(self, char):
        if (self.timer == self.maxtime):
            self.kill()
        self.timer += 1

class projectile(Hitboxes):
    def __init__(self, rect, time, type, atk, kb , speed, travel, heading):
        Hitboxes.__init__(self, rect, time, type, atk, kb)
        self.movespeed = speed
        self.maxtrav = travel
        self.heading = heading

    def move(self):
        if (self.heading == 0): #right
            self.rect = self.rect.move(self.movespeed, 0)
            
        elif(self.heading == 1): #left
            self.rect = self.rect.move(-self.movespeed, 0)
            
        elif(self.heading == 3): #up
            self.rect = self.rect.move(0, -self.movespeed)
            
        elif(self.heading == 2): #left
            self.rect = self.rect.move(0, self.movespeed)
        
    def update(self, char):
        if (getDistance(self.rect.center, char.rect.center) >= self.maxtrav):
            self.kill()
        self.move()

    
