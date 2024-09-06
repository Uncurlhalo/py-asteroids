import circleshape
import constants
import pygame
import shot

# Player class that inherits from CircleShape
class Player(circleshape.CircleShape):
    # constructor, we just super the circle
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    # draw our player polygon
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)

    # rotate our player
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    # move our player
    def move(self, dt):
        # make a forward vector
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self):
        my_shot = shot.Shot(self.position.x, self.position.y)
        my_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED

    # detect key presses and update
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a, pygame.K_RIGHT]:
            self.rotate(-dt)
        if keys[pygame.K_d, pygame.K_LEFT]:
            self.rotate(dt)
        if keys[pygame.K_w, pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s, pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    # give us the coordinates of our triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]