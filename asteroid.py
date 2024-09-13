import circleshape
import constants
import random
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw that circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(rand_angle)
        new_vel_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_ast_1.velocity = new_vel_1 * 1.2
        new_ast_2.velocity = new_vel_2 * 1.2
