import pygame

class Sound:
    def __init__(self, sounds, chan):
        self.sounds = sounds
        self.sbools = []
        for i in range(len(self.sounds)):
            self.sbools.append(False)
        self.channel = pygame.mixer.Channel(chan)
        self.prev = [None, None]

    def play(self, num, vol):
        if not self.sbools[num]:
            self.stop()
            self.sbools[num] = True
            self.channel.set_volume(vol)
            self.channel.play(self.sounds[num])

    def dirPlay(self, num, direc, vol):
        if self.prev != [vol, direc]:
            self.prev[0] = vol
            self.prev[1] = direc
            self.stop()
            self.sbools[num] = True
            if direc == 0:                              #LEFT
                self.channel.set_volume(vol/100, 0.0)
            elif direc == 1:                            #RIGHT
                self.channel.set_volume(0.0, vol/100)
            elif direc == 2:                            #Up or Down
                self.channel.set_volume(vol/100, vol/100)
            elif direc == 3:
                self.channel.set_volume(vol/200, vol/200)
            self.channel.play(self.sounds[num])

    def updateBools(self):
        if not self.channel.get_busy():
            self.stop()

    def stop(self):
        for i in range(len(self.sounds)):
            if self.sbools[i]:
                self.sbools[i] = False
            self.channel.stop()

    def setVolume(self, vol):
        '''int between 1 and 100'''
        self.channel.set_volume(vol/100)
