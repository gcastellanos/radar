import pygame
from pygame.locals import *
from Text import *

class Option:
    def __init__(self, text, font, handle = None, args = [], phandle = None, pargs = None):
        self.screen = pygame.display.get_surface()
        self.text = text
        self.font = font
        self.textBox = None
        self.center = None
        self.handle = handle
        self.args = args
        self.phandle = phandle
        self.pargs = pargs

    def setText(self):
        self.textBox = Text(self.center, self.font, True)
        self.textBox.changeText(self.text)

    def setCenter(self, center):
        self.center = center
        self.setText()

    def getCenter(self):
        return self.center

    def display(self, surf):
        self.textBox.display(surf)

    def go(self):
        if self.handle:
            self.handle(*self.args)

    def select(self):
        self.textBox.setUnderline(True)
        self.textBox.rerender()
        if self.phandle != None:
            self.phandle(*self.pargs)
        #self.textBox.setCenter(self.center)

    def deselect(self):
        self.textBox.setUnderline(False)
        self.textBox.rerender()
        #self.textBox.setCenter(self.center)
