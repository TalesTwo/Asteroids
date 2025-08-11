import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    containers = None

    # initializeing player class
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    # create triangle for the screen
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # draw player on the screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # rotate the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # move the player forward or back
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # create a shot and fire it forward
    def shoot(self, dt):
        if self.cooldown <= 0:
            shot = Shot(self.position[0], self.position[1])
            vector = pygame.Vector2(1, 0).rotate(self.rotation + 90)
            vector *= PLAYER_SHOOT_SPEED
            shot.velocity = vector
            self.cooldown = PLAYER_SHOOT_COOLDOWN
        else:
            self.cooldown -= dt

    # check for key presses, update obhect accordingly
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: # rotate player left
            self.rotate(dt * -1)
        if keys[pygame.K_d]: # rotate player right
            self.rotate(dt)
        if keys[pygame.K_w]: # move player forward
            self.move(dt)
        if keys[pygame.K_s]: # move player backward
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)