import pygame, random, math
from pygame.locals import *
from SoundInit import *
from Enemy import *
from landmarks import *
from DirFX import *
from weaponClass import *
from armorClass import *

class Spawner:
    def __init__(self, char, smanager, enemies, lmarks, dirfx, dirfxs, weaponChannel, armorChannel):
        self.char = char
        self.smanager = smanager
        self.enemies = enemies
        self.enemy_min_timer = 100
        self.enemy_max_timer = 500
        self.enemy_timer = 0
        self.enemy_min_dist = 1000
        self.enemy_max_dist = 1400
        self.lmarks = lmarks
        self.lmark_count = 100
        self.lmark_min_dist = 1300
        self.lmark_max_dist = 15000
        self.lmark_min_size = 500
        self.lmark_max_size = 1000
        self.lmark_kill_dist = 15000
        self.dirfx = dirfx
        self.dir_min_timer = 100
        self.dir_max_timer = 1000
        self.dir_timer = 0
        self.dir_min_dist = 1000
        self.dir_max_dist = 1400
        self.dir_max_count = 2
        self.dirfxs = dirfxs
        self.dirs_min_timer = 100
        self.dirs_max_timer = 1000
        self.dirs_timer = 0
        self.dirs_min_dist = 100
        self.dirs_max_dist = 1000
        self.dirs_max_count = 2
        self.weaponChannel = weaponChannel
        self.armorChannel = armorChannel
        self.loot = ["Katana", "BattleAxe", "Spear", "Pistol", "lightArmor", "mediumArmor",\
                     "poweredArmor", "actionherosArmor"]
        self.droprate = .3

    def createEquipment(self, string):
        if string == "Katana":
            return Katana(self.char, self.weaponChannel)
        elif string == "BattleAxe":
            return BattleAxe(self.char, self.weaponChannel)
        elif string == "Spear":
            return Spear(self.char, self.weaponChannel)
        elif string == "Pistol":
            return Pistol(self.char, self.weaponChannel)
        elif string == "lightArmor":
            return lightArmor(self.armorChannel)
        elif string == "mediumArmor":
            return mediumArmor(self.armorChannel)
        elif string == "lightArmor":
            return poweredArmor(self.armorChannel)
        elif string == "lightArmor":
            return actionheroesArmor(self.armorChannel)
        
    def collide(self, rect):
        for en in self.enemies:
            if rect.colliderect(en.rect):
                return True
        for lm in self.lmarks:
            if rect.colliderect(lm.rect):
                return True
        return False

    def updateEnemyTimer(self):
        if self.enemy_timer != 0:
            self.enemy_timer -= 1
        else:
            self.enemy_timer = random.randint(self.enemy_min_timer, self.enemy_max_timer)

    def updateDirTimer(self):
        if self.dir_timer != 0:
            self.dir_timer -= 1
        else:
            self.dir_timer = random.randint(self.dir_min_timer, self.dir_max_timer)

    def updateDirsTimer(self):
        if self.dirs_timer != 0:
            self.dirs_timer -= 1
        else:
            self.dirs_timer = random.randint(self.dirs_min_timer, self.dirs_max_timer)

    def spawnEnemy(self):
        if self.enemy_timer == 0:
            notDone = True
            while notDone:
                direc = random.randint(0, 359)
                dist = random.randint(self.enemy_min_dist, self.enemy_max_dist)
                x = dist * math.cos(math.radians(direc))
                y = -dist * math.sin(math.radians(direc))
                lootNum = random.randint(0, int(len(self.loot)/self.droprate))
                loot = None
                if lootNum < len(self.loot):
                    temp = self.loot[lootNum]
                    loot = self.createEquipment(temp)
                e = Zombie((x, y), self.smanager.get(), zombie_sounds, self.smanager, loot)
                notDone = self.collide(e.rect)
            self.enemies.add(e)
        self.updateEnemyTimer()

    def spawnLandMark(self):
        if len(self.lmarks) < self.lmark_count:
            notDone = True
            while notDone:
                direc = random.randint(0, 359)
                dist = random.randint(self.lmark_min_dist, self.lmark_max_dist)
                sizex = random.randint(self.lmark_min_size, self.lmark_max_size)
                sizey = random.randint(self.lmark_min_size, self.lmark_max_size)
                size = (sizex, sizey)
                x = dist * math.cos(math.radians(direc))
                y = -dist * math.sin(math.radians(direc))
                loc = (x, y)
                l = landmarks(size, loc, self.lmark_kill_dist)
                notDone = self.collide(l.rect)
            self.lmarks.add(l)

    def spawnDirFX(self):
        if self.dir_timer == 0 and len(self.dirfx) < self.dir_max_count:
            notDone = True
            while notDone:
                direc = random.randint(0, 359)
                dist = random.randint(self.dir_min_dist, self.dir_max_dist)
                x = dist * math.cos(math.radians(direc))
                y = -dist * math.sin(math.radians(direc))
                d = DirFX((x, y), dir_sounds, self.smanager.get(), self.smanager)
                notDone = self.collide(d.rect)
            self.dirfx.add(d)
        self.updateDirTimer()

    def spawnDirsFX(self):
        if self.dirs_timer == 0 and len(self.dirfxs) < self.dirs_max_count:
            notDone = True
            while notDone:
                direc = random.randint(0, 359)
                dist = random.randint(self.dirs_min_dist, self.dirs_max_dist)
                x = dist * math.cos(math.radians(direc))
                y = -dist * math.sin(math.radians(direc))
                d = DirFXs((x, y), dirs_sounds, self.smanager.get(), self.smanager)
                notDone = self.collide(d.rect)
            self.dirfxs.add(d)
        self.updateDirsTimer()












