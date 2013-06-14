import sys, re
from Init import *
from Menu import *
from EventHandlers import *
from charClass import *
from Enemy import *
from landmarks import * 
from SoundManager import *
from Events import *
from Spawner import *
from DirFX import *

class world():
    def __init__(self):
        self.pauseMenu = Menu()
        self.statsMenu = Menu()
        self.weaponMenu = Menu()
        self.armorMenu = Menu()
        self.promptMenu = Menu()
        self.rmin = 400
        self.rmax = 800
        self.bgtimer = random.randint(self.rmin, self.rmax)
        self.dirtimer = random.randint(self.rmin, self.rmax)
        self.max_chans = 100
        pygame.mixer.set_num_channels(self.max_chans)
        self.smanager = SoundManager(self.max_chans)
        amb = pygame.mixer.Sound('ambient2.ogg')
        self.ambch = pygame.mixer.Channel(self.smanager.get())
        br = pygame.mixer.Sound('charbreath.ogg')
        wk = pygame.mixer.Sound('charwalk.ogg')
        rn = pygame.mixer.Sound('charrun.ogg')
        gr = pygame.mixer.Sound('chargrunt.ogg')
        hw = pygame.mixer.Sound('hitwall2.ogg')
        hb = pygame.mixer.Sound('heartbeat.ogg')
        hbf = pygame.mixer.Sound('heartbeat_fast.ogg')
        
        pygame.mixer.Sound('armor_aquire.ogg')
        bgfx = [pygame.mixer.Sound('roar_distant.ogg'),\
                pygame.mixer.Sound('ambient3.ogg'),\
                pygame.mixer.Sound('bug_alien.ogg')]
        self.bgsound = RadarSound(bgfx, self.smanager.get())
        self.screen = pygame.display.get_surface()
        self.srect = self.screen.get_rect()
        self.bg = pygame.Surface((self.srect.width, self.srect.height))
        self.bg.fill((0, 75, 75))
        self.bgrect = self.bg.get_rect()
        self.fog = pygame.Surface((self.srect.width, self.srect.height))
        self.fog.fill((128, 128, 128))
        self.fogrect = self.fog.get_rect()
        self.fog.set_alpha(245)
        self.char = Char(self.smanager.get(), [wk, rn], self.smanager.get(), [br, gr, hw],\
                 self.smanager.get(), [hb, hbf])
        self.weaponChannel = self.smanager.get()
        self.armorChannel = self.smanager.get()
        self.char.getWeapon(Katana(self.char, self.weaponChannel))
        self.char.getWeapon(Pistol(self.char, self.weaponChannel))
        self.char.equipWeapon(0)
        self.char.getArmor(lightArmor(self.armorChannel))
        self.char.equipArmor(0)
        self.chars = pygame.sprite.RenderUpdates(self.char)
        self.enemies = pygame.sprite.RenderUpdates()
        self.lmarks = pygame.sprite.RenderUpdates()
        self.dirfx = pygame.sprite.RenderUpdates()
        self.dirfxs = pygame.sprite.RenderUpdates()
        self.spawner = Spawner(self.char, self.smanager, self.enemies, self.lmarks,\
                               self.dirfx, self.dirfxs, self.weaponChannel, self.armorChannel)
        self.menuInit()
        self.ambch.set_volume(.5)
        self.ambch.play(amb, -1)
        self.clock = pygame.time.Clock()
        self.bgdis()
        pygame.display.flip

    def menuInit(self):
        win = re.compile(r"win")
        linux = re.compile(r"linux")
        if win.match(sys.platform) != None:
            self.menuInitWindows()
        elif linux.match(sys.platform) != None:
            self.menuInitLinux()
    
    def menuInitWindows(self):
        tsize = 60
        osize = 60
        panel = Panel((200, 200), (self.srect.width - 200, self.srect.height - 200))
        panel.setTSize(40)
        panel.setOSize(50)
        self.promptMenu.addPanel(panel)
        panel.initOptions((panel.getCenter()[0] - 15, 70), 3, 60)
        panel.setTexts([Text((0, 0), panel.tsize)])
        
        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.pauseMenu.addPanel(panel)
        self.pauseMenu.addPanel(panel2)
        panel2.setTexts([Text((0, 0), 100)])
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.addOptions([Option("1: Stats", panel.osize, phandle = pauseMenuPrintStats,\
                                 pargs = [self.pauseMenu, self.char]),\
                          Option("2: Weapons", panel.osize, handle = pauseMenuRunWeapons,\
                                 args = [self.weaponMenu, self.char, self.promptMenu]),\
                          Option("3: Armor", panel.osize, handle = pauseMenuRunArmor,\
                                 args = [self.armorMenu, self.char, self.promptMenu])])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.statsMenu.addPanel(panel)
        self.statsMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.addOptions([Option("1: Back", panel.osize, generalBackButton, [])])
        panel2.setTexts([Text((panel2.getCenter()[0], 100), panel2.tsize, True)])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.weaponMenu.addPanel(panel)
        self.weaponMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.setTexts([Text((0, 0), panel.tsize)])
        panel2.setTexts([Text((0, 0), panel2.tsize)])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.armorMenu.addPanel(panel)
        self.armorMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.setTexts([Text((0, 0), panel.tsize)])
        panel2.setTexts([Text((0, 0), panel2.tsize)])

    def menuInitLinux(self):
        tsize = 85
        osize = 60
        panel = Panel((200, 200), (self.srect.width - 200, self.srect.height - 200))
        panel.setTSize(55)
        panel.setOSize(osize)
        self.promptMenu.addPanel(panel)
        panel.initOptions((panel.getCenter()[0] - 15, 70), 3, 60)
        panel.setTexts([Text((0, 0), panel.tsize)])
        
        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.pauseMenu.addPanel(panel)
        self.pauseMenu.addPanel(panel2)
        panel2.setTexts([Text((0, 0), 100)])
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.addOptions([Option("1: Stats", panel.osize, phandle = pauseMenuPrintStats,\
                                 pargs = [self.pauseMenu, self.char]),\
                          Option("2: Weapons", panel.osize, handle = pauseMenuRunWeapons,\
                                 args = [self.weaponMenu, self.char, self.promptMenu]),\
                          Option("3: Armor", panel.osize, handle = pauseMenuRunArmor,\
                                 args = [self.armorMenu, self.char, self.promptMenu])])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(osize)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.statsMenu.addPanel(panel)
        self.statsMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.addOptions([Option("1: Back", panel.osize, generalBackButton, [])])
        panel2.setTexts([Text((panel2.getCenter()[0], 100), panel2.tsize, True)])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(40)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.weaponMenu.addPanel(panel)
        self.weaponMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.setTexts([Text((0, 0), panel.tsize)])
        panel2.setTexts([Text((0, 0), panel2.tsize)])

        panel = Panel((400, 720), (0,0))
        panel2 = Panel((880, 720), (400, 0))
        panel.setTSize(tsize)
        panel.setOSize(40)
        panel2.setTSize(tsize)
        panel2.setOSize(osize)
        self.armorMenu.addPanel(panel)
        self.armorMenu.addPanel(panel2)
        panel.initOptions((panel.getCenter()[0] - 15, 100), 6)
        panel.setTexts([Text((0, 0), panel.tsize)])
        panel2.setTexts([Text((0, 0), panel2.tsize)])

    def playBGM(self):
        self.bgsound.updateBools()
        if self.bgtimer == 0:
            self.bgsound.play(random.randint(0, len(self.bgsound.sounds) - 1), .5)
            self.bgtimer = random.randint(self.rmin, self.rmax)
        else:
            self.bgtimer -= 1

    def playDir(self):
        for d in self.dirfx:
            d.proximity(self.char)

    def collide(self):
        for en in self.enemies:
            if self.char.rect.colliderect(en.rect):
                self.char.damage(en.attack)
                en.knockback(self.char.rect, en.knockback_dist, self.lmarks)
        for hb in self.char.hitboxes:
            for en in self.enemies:
                if hb.rect.colliderect(en.rect):
                    en.rsound.stop()
                    en.damage(hb.attack)
                    en.knockback(hb.rect, hb.kb, self.lmarks)
                    if en.isDead():
                        en.rsound.play(7, .5)
                        self.char.pickup(en.drop())
                        en.die()
                        self.char.killcount += 1
                    else:
                        en.rsound.play(6, .5)
                    hb.kill()
                    #self.char.selectHBSound(hb)
            for lm in self.lmarks:
                if lm.rect.colliderect(hb.rect):
                    hb.kill()

    def eventloop(self):
        while True:
            self.clock.tick(24)
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    print("You quit... thats unfortunate, but your score was: ", self.char.killcount)
                    return
                if event.type == CHARDEATH:
                    print( "Congratulations... you died. Good job! your score is: ", self.char.killcount)
                    return
                if event.type == KEYDOWN and event.key == K_p:
                    try:
                        self.char.rsound.stop()
                        self.char.rsound3.stop()
                        runPauseMenu(self.pauseMenu, self.char)
                        self.bgdis()
                        #exself.endis()
                        #self.chardis()
                        pygame.display.flip()
                    except SystemExit:
                        return
                if event.type == KEYDOWN and event.key == K_j:
                    self.char.attack()
            self.char.update()
            self.lmarks.update(self.char)
            self.playBGM()
            self.playDir()
            self.enemies.update(self.char, self.lmarks)
            self.scroll()
            self.bgdis()
            self.endis()
            self.chardis()
            self.lmdis()
            self.fogdis()
            pygame.display.flip()
            self.collide()
            self.char.weapon.updatecooldown()
            self.char.hitboxes.update(self.char)
            self.spawner.spawnEnemy()
            self.spawner.spawnLandMark()
            self.spawner.spawnDirFX()
            '''for h in self.char.hitboxes:
            print(h, ",", end='')
            print()'''
        
    def scroll(self):
        tup = self.char.move(self.lmarks)
        for lm in self.lmarks:
            lm.scroll(tup)
        for en in self.enemies:
            en.scroll(tup)
        for d in self.dirfx:
            d.scroll(tup)

    def prox(self):
        for en in self.enemies:
            self.char.proximity(en)

    def fogdis(self):
        self.screen.blit(self.fog, self.fogrect)

    def bgdis(self):
        self.screen.blit(self.bg, self.bgrect)

    def chardis(self):
        '''self.chars.clear(self.screen, self.bg)
        pygame.display.update(self.chars.draw(self.screen))'''
        self.screen.blit(self.char.image, self.char.rect)
    
    def endis(self):
        '''self.spawner.enemies.clear(self.screen, self.bg)
        pygame.display.update(self.enemies.draw(self.screen))'''
        for en in self.enemies:
            self.screen.blit(en.image, en.rect)

    def lmdis(self):
        '''self.lmarks.clear(self.screen, self.bg)
        pygame.display.update(self.lmarks.draw(self.screen))'''
        for lm in self.lmarks:
            self.screen.blit(lm.image, lm.rect)

