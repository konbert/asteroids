import pygame
import random
from circleshape import CircleShape
from constants import *

white = (255, 255, 255)

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, white,self.position, self.radius, 2 )

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = v1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, radius)
        asteroid.velocity = v2 * 1.2


