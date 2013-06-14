import pygame
from pygame.locals import *
from MyUtils import *
from RadarSound import *

class Armor:
    def __init__(self, defense, description, type, chan):
        self.defense = defense
        self.description = description
        self.type = type
        self.rsound = RadarSound([pygame.mixer.Sound('armor_aquire.ogg')], chan)

class lightArmor(Armor):
    def __init__(self, chan):
        Armor.__init__(self, 1, "This armor is better than your shirt barely",\
                       "Light Armor", chan)


class mediumArmor(Armor):
    def __init__(self, chan):
        Armor.__init__(self, 1, "This armor is just alright",\
                       "Medium Armor", chan)

class poweredArmor(Armor):
    def __init__(self, chan):
        Armor.__init__(self, 2, "This armor is layered Titanium plates offering strong protection",\
                       "Powered Armor", chan)


class actionherosArmor(Armor):
    def __init__(self, chan):
        Armor.__init__(self, 3, "This armor while consisting of no material that offers protection somehow makes you near invulenerable",\
                       "Action Hero's Armor", chan)
