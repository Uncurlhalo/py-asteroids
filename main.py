#!/usr/bin/env python
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # init and set resolution
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Check for QUIT events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # fill display with black and update
        screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()