import pygame, os

os.environ['SDL_VIDEO_WINDOW_POS'] = '500,500'
pygame.mixer.pre_init(44100, -16, 8, 1024)
pygame.init()
pygame.display.set_mode((1280, 720))
