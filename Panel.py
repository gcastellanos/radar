import pygame
from pygame.locals import *
from Text import *
from Option import *

class Panel:
    def __init__(self, dim, topleft):
        self.screen = pygame.display.get_surface()
        self.outlineWidth = 2
        self.borderWidth = 8
        self.outline = pygame.Surface(dim)
        self.outlineRect = self.outline.get_rect()
        self.outlineRect.topleft = topleft
        self.border = pygame.Surface((self.outlineRect.width - (2 * self.outlineWidth),\
                                      self.outlineRect.height - (2 * self.outlineWidth)))
        self.borderRect = self.border.get_rect()
        self.borderRect.topleft = (self.outlineRect.left + self.outlineWidth,\
                                   self.outlineRect.top + self.outlineWidth)
        self.panel = pygame.Surface((self.borderRect.width - (2 * self.borderWidth),\
                                     self.borderRect.height - (2 * self.borderWidth)))
        self.panelRect = self.panel.get_rect()
        self.panelRect.topleft = (self.borderRect.left + self.borderWidth,\
                                  self.borderRect.top + self.borderWidth)
        self.border.fill((255, 255, 255))
        self.panelColor = (100, 255, 100)
        self.panel.fill(self.panelColor)
        self.texts = []
        self.options = []
        self.option_loc = None
        self.option_vbuf = None
        self.option_min = None
        self.option_range = None
        self.tsize = 60
        self.osize = 60
        self.selected = None
        self.tselected = None

    def setTSize(self, value):
        self.tsize = value

    def setOSize(self, value):
        self.osize = value

    def printOption(self):
        if self.selected != None:
            print(self.options[self.selected].text)

    def optionShiftUp(self):
        for op in self.options:
            op.setCenter((op.getCenter()[0], op.getCenter()[1] - self.option_vbuf))

    def optionShiftDown(self):
        for op in self.options:
            op.setCenter((op.getCenter()[0], op.getCenter()[1] + self.option_vbuf))

    def printText(self):
        if self.tselected != None:
            print(self.texts[self.tselected].text)

    def textDown(self):
        if self.tselected != None and self.tselected + 1 < len(self.texts):
            self.tselected += 1
            print(self.texts[self.selected].text)

    def textUp(self):
        if self.tselected != None and self.tselected > 0:
            self.tselected -= 1
            print(self.texts[self.selected].text)

    def cursorDown(self):
        if self.selected != None and self.selected + 1 < len(self.options):
            self.options[self.selected].deselect()
            self.selected += 1
            if self.selected == self.option_min + self.option_range:
                self.option_min += 1
                self.optionShiftUp()
            print(self.options[self.selected].text)
            self.options[self.selected].select()

    def cursorUp(self):
        if self.selected != None and self.selected > 0:
            self.options[self.selected].deselect()
            self.selected -= 1
            if self.selected < self.option_min:
                self.option_min -= 1
                self.optionShiftDown()
            print(self.options[self.selected].text)
            self.options[self.selected].select()

    def select(self):
        if self.selected != None:
            self.options[self.selected].go()

    def getCenter(self):
        return (self.outlineRect.width / 2, self.outlineRect.height / 2)

    def getMaxWidth(self):
        return self.outlineRect.width - (2 * (self.outlineWidth + self.borderWidth))

    def textExists(self, index):
        return index < len(self.texts)

    def draw(self):
        self.screen.blit(self.outline, self.outlineRect)
        self.screen.blit(self.border, self.borderRect)
        self.screen.blit(self.panel, self.panelRect)

    def setTexts(self, texts):
        self.texts = texts
        if len(self.texts) > 0:
            self.tselected = 0

    def changeText(self, text, index):
        self.texts[index].changeText(text)

    def initOptions(self, loc, option_range, ovbuf = 100):
        self.option_loc = loc
        self.option_range = option_range
        self.option_vbuf = ovbuf

    def clearOptions(self):
        self.options = []
        self.selected = None

    def addOptions(self, options):
        for op in options:
            if len(self.options) == 0:
                self.option_min = 0
                op.setCenter(self.option_loc)
            else:
                c = self.options[-1].getCenter()
                op.setCenter((c[0], c[1] + self.option_vbuf))
            self.options.append(op)
        if len(self.options) > 0 and self.selected == None:
            self.selected = 0
            self.options[self.selected].select()

    def setOptions(self, options):
        self.options = options
        if len(self.options) > 0:
            self.selected = 0
            self.options[self.selected].select()

    def write(self):
        self.panel.fill(self.panelColor)
        for t in self.texts:
            t.display(self.panel)

    def drawOptions(self):
        if self.option_min != None:
            last = self.option_min + self.option_range
            if len(self.options) < last:
                last = len(self.options)
            for i in range(self.option_min, last):
                self.options[i].display(self.panel)

    def update(self):
        self.write()
        self.drawOptions()
        self.draw()
