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

    # make a player
    x_spawn, y_spawn = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
    my_player = player.Player(x_spawn, y_spawn)

    # Event loop
    while True:
        # Check for QUIT events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill with black, update rotation, draw player
        screen.fill("black")
        my_player.update(dt)
        my_player.draw(screen)
        # update display
        pygame.display.flip()

        # tick the clock and save to delta 
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()