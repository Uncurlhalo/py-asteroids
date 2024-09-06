#!/usr/bin/env python
import pygame
from constants import *

def main():
    # init and set resolution
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # setup a clock and delta variable
    clock = pygame.time.Clock()
    dt = 0

    # Event loop
    while True:
        # Check for QUIT events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill display with black and update
        screen.fill((0,0,0))
        pygame.display.flip()

        # tick the clock and save to delta 
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()