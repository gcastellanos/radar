from MenuInit import *

def main():
    screen = pygame.display.get_surface()
    area = screen.get_rect()
    bg = pygame.Surface((area.width, area.height))
    bgrect = bg.get_rect()
    try:
        mainMenu.run()
    except SystemExit:
        return
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_q:
                return
        screen.blit(bg, bgrect)
        pygame.display.flip()

main()
pygame.quit()
