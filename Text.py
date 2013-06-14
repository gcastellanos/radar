import pygame
from pygame.locals import *

class Text:
    def __init__(self, topleft, size = 30, centered = False, maxwidth = None):
        self.text = ''
        self.size = size
        self.font = pygame.font.SysFont("Calibri", self.size)
        self.vbuf = self.font.get_linesize()
        self.hbuf = 15
        self.centered = centered
        if maxwidth:
            self.maxW = maxwidth - (2 * self.hbuf)
        else:
            self.maxW = None
        self.topleft = (topleft[0], topleft[1])
        self.images = []

    def setUnderline(self, u):
        self.font.set_underline(u)

    def setCenter(self, center):
        self.images[0][1].center = center

    def changeText(self, text):
        self.images = []
        self.text = text
        self.render()

    def rerender(self):
        self.images = []
        self.render()

    def display(self, surf):
        for image in self.images:
            surf.blit(image[0], image[1])

    def render(self):
        lines = self.text.split("\n")
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        lines2 = []
        i = 0
        spaceBool = True
        if self.maxW:
            for line in lines:
                lines2.append(line)
                while True:
                    if self.font.size(lines2[i])[0] > self.maxW:
                        if len(lines2) - 1 < i + 1:
                            lines2.append("")
                        part = lines2[i].rpartition(" ")
                        if part[0] == '':
                            part = (lines2[i][:-1], lines2[i][-1])
                            lines2[i] = part[0]
                            if spaceBool:
                                lines2[i + 1] = part[1] + " " + lines2[i + 1]
                                spaceBool = False
                            else:
                                lines2[i + 1] = part[1] + lines2[i + 1]
                        else:
                            lines2[i] = part[0]
                            if lines2[i + 1] != "":
                                lines2[i + 1] = part[2] + " " + lines2[i + 1]
                            else:
                                lines2[i + 1] = part[2]
                    else:
                        i += 1
                        spaceBool = True
                        if len(lines2) == i or\
                           not self.font.size(lines2[i])[0] > self.maxW:
                            break
        else:
            lines2 = lines
        topleft = self.topleft
        for line in lines2:
            tempImage = self.font.render(line, False, (255,255,255))
            tempRect = tempImage.get_rect()
            if self.centered:
                tempRect.center = topleft
            else:
                tempRect.topleft = topleft
            topleft = (topleft[0], topleft[1] + self.vbuf)
            self.images.append((tempImage, tempRect))
