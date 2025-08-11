import pygame
from constants import *
from player import Player

def main():

    # creating pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting game clock
    clock = pygame.time.Clock()
    dt = 0

    # creating player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # infinite game loop
    while(1):
        for event in pygame.event.get():    # reading events
            if event.type == pygame.QUIT:
                return
        screen.fill("black")                # filling the screen "black"
        player.draw(screen)                 # drawing player to screen
        pygame.display.flip()               # refreshing the screen
        # running at 60 FPS maximum
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
