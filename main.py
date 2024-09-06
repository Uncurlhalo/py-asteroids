#!/usr/bin/env python
import pygame
import player
from constants import *

def main():
    # init and set resolution
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # setup a clock and delta variable
    clock = pygame.time.Clock()
    dt = 0

    # make my groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add player container to the groups
    player.Player.containers = (updatable, drawable)
    # make my player
    x_spawn, y_spawn = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    my_player = player.Player(x_spawn, y_spawn)

    # Event loop
    while True:
        # Check for QUIT events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update objects
        for obj in updatable:
            obj.update(dt)

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