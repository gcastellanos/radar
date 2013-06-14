import pygame
from pygame.locals import *
from MyUtils import *
from hitboxes import *
from RadarSound import *


class Weapon:
    def __init__(self, char, attack, hrect, vrect, knockback, discription, time, cdtime, sounds, chan, type):
        self.char = char
        self.hrect = hrect
        self.knockback = knockback
        self.vrect = vrect
        self.attack = attack
        self.text = discription
        self.cooldown = 0
        self.cooldown_time = cdtime
        self.maxtime = time
        self.rsound = RadarSound(sounds, chan)
        self.type = type

    def updatecooldown(self):
        if self.cooldown != 0:
            self.cooldown += 1
            self.cooldown %= self.cooldown_time

    def coolDown(self):
        if self.cooldown != 0:
            return False
        else:
            return True
            

class Sword(Weapon):
    def __init__(self, char, attack, hrect, vrect, knockback, discription, time, cdtime, sounds, chan, type):
        Weapon.__init__(self, char, attack, hrect,vrect, knockback, discription, time, cdtime, sounds, chan, type)

        
    def doAttack(self):
        direc = self.char.wheading
        if (self.coolDown()):
            self.cooldown = 1
            self.rsound.updateBools()
            self.rsound.play(0, .3)
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
            return Hitboxes(rect, self.maxtime, self.type, self.attack, self.knockback)


class Katana(Sword):
    def __init__(self, char, chan):
        Sword.__init__(self, char, 5, pygame.Rect(0,0,30,30), pygame.Rect(0,0,30,30),\
                       50,"This is a Katana, it has a narrow but deadly attack", 4, 6,\
                       [pygame.mixer.Sound('swordswing2.ogg'),\
                        pygame.mixer.Sound('weapon_aquire.ogg')], chan, 'Katana')

class BattleAxe(Sword):
    def __init__(self, char, chan):
        Sword.__init__(self, char, 20, pygame.Rect(0,0,20,60), pygame.Rect(0,0,60,20),\
                       100, "BattleAxes have a wide but narrow attack", 4, 24,\
                       [pygame.mixer.Sound('axeswing.ogg'), pygame.mixer.Sound('weapon_aquire.ogg')],\
                       chan, 'Battle Axe')

class Spear(Sword):
    def __init__(self, char, chan):
        Sword.__init__(self, char, 10, pygame.Rect(0,0,70,10), pygame.Rect(0,0,10,70),\
                       70, "Spears have a long narrow attack", 4, 12,\
                       [pygame.mixer.Sound('spearthrust.ogg'), pygame.mixer.Sound('weapon_aquire.ogg')],\
                       chan, 'Spear')

class Gun(Weapon):
    def __init__(self, char, attack, hrect, vrect, knockback, description, time, cdtime,\
                 sounds, chan, type, maxspeed, maxtravel):
        Weapon.__init__(self, char, attack, hrect,vrect, knockback, description, time, cdtime, sounds, chan, type)
        self.maxspeed = maxspeed
        self.maxtravel = maxtravel
        

    def doAttack(self):
        direc = self.char.wheading
        if (self.coolDown()):
            self.cooldown = 1
            self.rsound.updateBools()
            self.rsound.play(0, .3)
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
            return projectile(rect, self.maxtime, self.type, self.attack,\
                              self.knockback, self.maxspeed, self.maxtravel, direc)

class Pistol(Gun):
    def __init__(self, char, chan):
        Gun.__init__(self, char, 5, pygame.Rect(0,0,5,5), pygame.Rect(0,0,5,5), 10,\
                     "A basic pistol with good range", 4, 12,\
                     [pygame.mixer.Sound('pistol.ogg'), pygame.mixer.Sound('weapon_aquire.ogg')],\
                     chan, "Pistol", 25, 2000)














