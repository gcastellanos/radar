import pygame, random
from pygame.locals import *
from Circle import *
from MyUtils import *
from RadarSound import *
from Events import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, loc, chan, sounds, time, attack, health, smanager, loot):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.image = pygame.Surface((50, 50))
        self.image.fill((80, 80 , 80))
        self.rect = self.image.get_rect()
        self.rect.center = loc
        self.notice_dist = 900
        self.move_dist = 5
        self.knockback_dist = 120
        self.action = 0    #0,5,6,7,8:wait, 1:up, 2:down, 3:left, 4:right
        self.health = health
        self.rsound = RadarSound(sounds, chan)
        self.cooldown = 0
        self.maxtime = time
        self.attack = attack
        self.smanager = smanager
        self.loot = loot

    def drop(self):
        return self.loot

    def die(self):
        self.smanager.returnChan(self.rsound.cid)
        self.kill()

    def knockback(self, rect, val, lmarks):
        direc = getDirection(self.rect.center, rect.center)
        if isLeft(direc):
            self.rect = self.rect.move(val, 0)
            for lm in lmarks:
                if self.rect.colliderect(lm.rect):
                    self.rect.right = lm.rect.left
        elif isRight(direc):
            self.rect = self.rect.move(-val, 0)
            for lm in lmarks:
                if self.rect.colliderect(lm.rect):
                    self.rect.left = lm.rect.right
        elif isUp(direc):
            self.rect = self.rect.move(0, val)
            for lm in lmarks:
                if self.rect.colliderect(lm.rect):
                    self.rect.bottom = lm.rect.top
        else:
            self.rect = self.rect.move(0, -val)
            for lm in lmarks:
                if self.rect.colliderect(lm.rect):
                    self.rect.top = lm.rect.bottom

    def damage( self, hit):
        self.health -= hit
        print(self.health)

    def isDead(self):
        return self.health <= 0

    def hitLmarks(self, lmarks):
        for l in lmarks:
            if self.action == 1:
                newpos = self.rect.move(0, - self.move_dist)
            if self.action == 2:
                newpos = self.rect.move(0, self.move_dist)
            if self.action == 3:
                newpos = self.rect.move(- self.move_dist, 0)
            if self.action == 4:
                newpos = self.rect.move(self.move_dist, 0)
            else:
                newpos = self.rect
            if newpos.colliderect(l.rect):
                return True
        return False

    def proximity(self, char):
        direc = getDirection(char.rect.center, self.rect.center)
        dist = getDistance(char.rect.center, self.rect.center)
        self.rsound.updateBools()
        for i in range(7):
            if char.circles[i].collideRect(self.rect):
                if isLeft(direc):
                    if self.notice(char):
                        x = 5
                    else:
                        x = 2
                    n = 0
                elif isRight(direc):
                    if self.notice(char):
                        x = 5
                    else:
                        x = 2 
                    n = 1
                elif isUp(direc):
                    if self.notice(char):
                        x = 3
                    else:
                        x = 0 
                    n = 2
                else:
                    if self.notice(char):
                        x = 4
                    else:
                        x = 1 
                    n = 3
                if not self.rsound.sbools[6]:
                    self.rsound.dirPlay(x, n, 2 ** (6 - i))
                return
        self.die()

    def proximity2(self, char):
        direc = getDirection(char.rect.center, self.rect.center)
        dist = getDistance(char.rect.center, self.rect.center)
        self.rsound.updateBools()
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
        self.rsound.dirPlay(x, n, 100 - dist / 20)

    def updatecooldown(self):
        if self.cooldown != 0:
            self.cooldown += 1
            self.cooldown %= self.maxtime

    def coolDown(self):
        return self.cooldown != 0
    
    def hitTop(self):
        return self.rect.top - self.move_dist < 0

    def hitBottom(self):
        return self.rect.bottom + self.move_dist > self.area.bottom

    def hitLeft(self):
        return self.rect.left - self.move_dist < 0

    def hitRight(self):
        return self.rect.right + self.move_dist > self.area.right

    def notice(self, char):
        return getDistance(self.rect.center, char.rect.center) < self.notice_dist

    def move(self):
        if self.action == 1:
            newpos = self.rect.move(0, - self.move_dist)
            self.rect = newpos
        if self.action == 2:
            newpos = self.rect.move(0, self.move_dist)
            self.rect = newpos
        if self.action == 3:
            newpos = self.rect.move(- self.move_dist, 0)
            self.rect = newpos
        if self.action == 4:
            newpos = self.rect.move(self.move_dist, 0)
            self.rect = newpos

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

class Zombie(Enemy):
    def __init__(self, loc, chan, sounds, smanager, loot):
        Enemy.__init__(self, loc, chan, sounds, 42, 4, 20, smanager, loot)
        self.timer = 0
        self.delay = 30

    def updateTimer(self):
        if self.timer == 0:
            self.action = random.randint(0, 8)
        self.timer += 1
        self.timer %= self.delay
        
    def update(self, char, lmarks):
        self.updatecooldown()
        if not self.coolDown():
            self.proximity(char)
            self.cooldown = 1
        if self.notice(char):
            self.seek(char, lmarks)
        elif not self.hitLmarks(lmarks):
            self.move()
        self.updateTimer()

    def seek(self, char, lmarks):
        mult = 24
        direc = getDirection(self.rect.center, char.rect.center)
        x = self.move_dist * math.cos(math.radians(direc))
        y = -self.move_dist * math.sin(math.radians(direc))
        movex = self.rect.move(x, 0)
        movey = self.rect.move(0, y)
        movexy = self.rect.move(x, y)
        for l in lmarks:
            if movex.colliderect(l.rect):
                x = 0
            elif movey.colliderect(l.rect):
                y = 0
            elif movexy.colliderect(l.rect):
                x = 0
                y = 0
        self.rect = self.rect.move(x, y)
