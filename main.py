import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():

    # creating pygame screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setting game clock
    clock = pygame.time.Clock()
    dt = 0

    # creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # adding objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)

    # creating player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)    

    field = AsteroidField()

    # infinite game loop
    while(1):
        for event in pygame.event.get():    # reading events
            if event.type == pygame.QUIT:
                return
        screen.fill("black")                # filling the screen "black"
        updatable.update(dt)                # updating objects
        for shape in drawable:              # drawing objects to the screen
            shape.draw(screen)                
        pygame.display.flip()               # refreshing the screen
        # running at 60 FPS maximum
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
