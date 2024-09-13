#!/usr/bin/env python
import sys
import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    # init and set resolution
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # setup a clock and delta variable
    clock = pygame.time.Clock()
    dt = 0

    # Group stuff
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player stuff
    Player.containers = (updatable, drawable)
    x_spawn, y_spawn = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    my_player = Player(x_spawn, y_spawn)

    # Asteroid stuff
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    my_asteroid_field = AsteroidField()

    # Shot stuff
    Shot.containers = (shots, updatable, drawable)

    # Event loop
    while True:
        # Check for QUIT events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # update objects
        for obj in updatable:
            obj.update(dt)

        # check for collisions w/ players
        for asteroid in asteroids:
            if my_player.collision(asteroid):
                print("Game over!")
                sys.exit()
            # check shot collisions
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.kill()
                    shot.kill()
        
        # fill display with black
        screen.fill("black")

        # draw objects
        for obj in drawable:
            obj.draw(screen)
        
        # update display
        pygame.display.flip()

        # tick the clock and save to delta 
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()