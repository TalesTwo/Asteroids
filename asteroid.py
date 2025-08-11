import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw asteroid on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    # update asteroids current position
    def update(self, dt):
        self.position += (self.velocity * dt)
