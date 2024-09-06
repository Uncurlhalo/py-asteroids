import circleshape
import constants
import pygame

# Player class that inherits from CircleShape
class Player(circleshape.CircleShape):
    # constructor, we just super the circle
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)
    
    # triangle class to draw our little ship
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
