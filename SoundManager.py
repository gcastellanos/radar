import pygame

class SoundManager:
    def __init__(self, num):
        self.available = []
        for i in range(0, num):
            self.available.append(i)
        self.full = False
       

    def get(self):
        if not self.full:
            tmp = self.available.pop(0)
            return tmp
    
    def returnChan(self, num):
        self.available.append(num)
        if self.full:
            self.full = False
