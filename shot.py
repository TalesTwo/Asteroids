import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # draw shot on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    # update shots current position
    def update(self, dt):
        self.position += (self.velocity * dt)