import pygame
from pygame.locals import *
from Panel import *
from Text import *

class Menu:
    def __init__(self):
        self.panels = []
        self.focus = 0

    def setFocus(self, focus):
        self.focus = focus

    def addPanel(self, panel):
        self.panels.append(panel)

    def update(self):
        for panel in self.panels:
            panel.update()
        pygame.display.flip()

    def addText(self, text, panel, tbox):
        self.panels[panel].changeText(text, tbox)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_i:
                    return
                elif event.type == KEYDOWN and (event.key == K_w or event.key == K_UP):
                    self.panels[self.focus].cursorUp()
                elif event.type == KEYDOWN and (event.key == K_s or event.key == K_DOWN):
                    self.panels[self.focus].cursorDown()
                elif event.type == KEYDOWN and event.key == K_a:
                    self.panels[self.focus].textUp()
                elif event.type == KEYDOWN and event.key == K_d:
                    self.panels[self.focus].textDown()
                elif event.type == KEYDOWN and event.key == K_q:
                    self.focus = (self.focus - 1) % len(self.panels)
                    print("Panel ", self.focus)
                    self.panels[self.focus].printText()
                elif event.type == KEYDOWN and event.key == K_e:
                    self.focus = (self.focus + 1) % len(self.panels)
                    print("Panel ",self.focus)
                    self.panels[self.focus].printText()
                elif event.type == KEYDOWN and event.key == K_j:
                    self.panels[self.focus].select()
                elif event.type == KEYDOWN and event.key == K_p:
                    self.panels[self.focus].printText()
                elif event.type == KEYDOWN and event.key == K_o:
                    self.panels[self.focus].printOption()
            self.update()
