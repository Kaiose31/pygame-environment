import pygame,sys


def main():
    #VARIABLES
    WIDTH = 1000
    HEIGHT = 800
    BG =  (0,255,0)
    ROAD = (20,20,20)
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('DRIVER SIMULATION')
    screen.fill(BG)

    #draw road
    pygame.draw.rect(screen,ROAD,(0,HEIGHT/3,WIDTH,HEIGHT/3))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
main()