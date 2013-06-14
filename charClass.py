import pygame
from pygame.locals import *
from Circle import *
from MyUtils import *
from weaponClass import *
from armorClass import *
from RadarSound import *
from Events import *

class Char(pygame.sprite.Sprite):
    def __init__(self, chan1, sounds1, chan2, sounds2, chan3, sounds3):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 200, 50))
        self.rect = self.image.get_rect()
        self.rect.center = self.area.center
        self.move_dist = 7
        self.run_dist = 12
        self.circles = [Circle(200, self.rect.center), Circle(400, self.rect.center),\
                        Circle(700, self.rect.center), Circle(1000, self.rect.center),\
                        Circle(1300, self.rect.center), Circle(1600, self.rect.center),\
                        Circle(1900, self.rect.center), Circle(2200, self.rect.center)]
        self.weapon = None
        self.armor = None
        self.weapons = []
        self.armors = []
        self.heading = 0
        self.movespeed = 0
        self.wheading = 0
        self.rsound = RadarSound(sounds1, chan1)
        self.rsound2 = RadarSound(sounds2, chan2)
        self.rsound3 = RadarSound(sounds3, chan3)
        self.hitboxes = pygame.sprite.Group()
        self.maxHealth = 20
        self.health = self.maxHealth
        self.h_regen_speed = 24 * 120
        self.invincible = 0
        self.invincible_time = 18
        self.killcount = 0

    def healthRegen(self):
        if self.health < self.maxHealth:
            self.health += (self.maxHealth / self.h_regen_speed)
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def updateInvincibilityTimer(self):
        if self.invincible > 0:
            self.invincible -= 1

    def isInvincible(self):
        return self.invincible != 0

    def update(self):
        if not self.rsound2.isBusy():
            self.rsound2.playNumTimes(0, .25, -1)
        if self.health <= (.25 * self.maxHealth):
            self.rsound3.play(1, 1, -1)
        elif self.health <= (.5 * self.maxHealth):
            self.rsound3.playNumTimes(0, .5, -1)
        else:
            self.rsound3.stop()
        self.updateInvincibilityTimer()
        self.healthRegen()

    def selectHBSound(self, hb):
        if hb.type == 'katana':
            self.rsound3.play(0, .5)

    def equipWeapon(self, ind):
        self.weapon = self.weapons[ind]

    def equipArmor(self, ind):
        self.armor = self.armors[ind]

    def pickup(self, item):
        if isinstance(item, Sword):
            self.getWeapon(item)
            item.rsound.play(1, .5)
        elif isinstance(item, Armor):
            self.getArmor(item)
            item.rsound.play(0, .5)

    def getWeapon(self, weapon):
        self.weapons.append(weapon)

    def getArmor(self, armor):
        self.armors.append(armor)

    def hitTop(self, lms, dist):
        for lm in lms:
            if self.rect.move(0, -dist).colliderect(lm.rect):
                return True
        return False

    def hitBottom(self, lms, dist):
        for lm in lms:
            if self.rect.move(0, dist).colliderect(lm.rect):
                return True
        return False

    def hitLeft(self, lms, dist):
        for lm in lms:
            if self.rect.move(-dist, 0).colliderect(lm.rect):
                return True
        return False

    def hitRight(self, lms, dist):
        for lm in lms:
            if self.rect.move(dist, 0).colliderect(lm.rect):
                return True
        return False

    def collideLms(self, lms, dist):
        return (self.hitTop(lms, dist) and (pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP])) or\
               (self.hitBottom(lms, dist) and (pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN])) or\
               (self.hitLeft(lms, dist) and (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT])) or\
               (self.hitRight(lms, dist) and (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]))

    def move(self, lms):
        vol = 1
        hvol = 1
        self.rsound.updateBools()
        self.rsound3.updateBools()
        dist = self.move_dist
        wk = 0
        if pygame.key.get_pressed()[K_SPACE]:
            dist = self.run_dist
            wk = 1
        if (pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]) and not self.hitTop(lms, dist):       #Up
            if pygame.key.get_pressed()[K_a] and not self.hitLeft(lms, dist):
                self.heading = 4
            elif pygame.key.get_pressed()[K_d] and not self.hitRight(lms, dist):
                self.heading = 5
            else:
                self.heading = 3
                self.wheading = 3
            self.movespeed = dist
            self.rsound.playNumTimes(wk, vol,-1)
        elif (pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]) and not self.hitBottom(lms, dist):  #Down
            if pygame.key.get_pressed()[K_a] and not self.hitLeft(lms, dist):
                self.heading = 6
            elif pygame.key.get_pressed()[K_d] and not self.hitRight(lms, dist):
                self.heading = 7
            else:
                self.heading = 2
                self.wheading = 2
            self.movespeed = dist
            self.rsound.playNumTimes(wk, vol,-1)
        elif (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]) and not self.hitLeft(lms, dist):    #Left
            self.heading = 1
            self.wheading = 1
            self.movespeed = dist
            self.rsound.playNumTimes(wk, vol,-1)
        elif (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]) and not self.hitRight(lms, dist):  #Right
            self.heading = 0
            self.wheading = 0
            self.movespeed = dist
            self.rsound.playNumTimes(wk, vol,-1)
        else:
            self.movespeed = 0
            self.rsound.stop()
        if self.collideLms(lms, dist):
            self.rsound2.play(2, hvol)
        #print(self.movespeed,self.heading)
        return self.movespeed,self.heading
        

    '''def proximity(self, en):
        direc = getDirection(self.rect.center, en.rect.center)
        for i in range(7):
            if self.circles[i].collideRect(en.rect):
                if isLeft(direc):
                    n = 0
                    x = 2
                elif isRight(direc):
                    n = 1
                    x = 2
                elif isUp(direc):
                    n = 2
                    x = 0
                else:
                    n = 3
                    x = 1
                en.rsound.dirPlay(x, n, 2 ** (7 - i))
                return
        en.rsound.prev = [None, None]'''

    def setHealth( self, num):
        self.health = num

    def attack(self):
        hb = self.weapon.doAttack()
        if hb != None:
            self.hitboxes.add(hb)

    def isDead(self):
        return self.health <= 0


    def damage(self, hit):
        if not self.isInvincible():
            if self.armor != None:
                hit -= self.armor.defense
                if hit < 0:
                    hit = 0
            self.health -= hit
            self.invincible = self.invincible_time
            self.rsound2.stop()
            self.rsound2.play(1, 1)
            if self.isDead():
                pygame.event.post(pygame.event.Event(CHARDEATH, {}))





