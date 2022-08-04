#!/usr/bin/env python3
"""A simple skiing game.

Day-iteration:
0-1: Screen with stationary rectangle
"""
import pygame


BOARD_SIZE = 480, 640
FRAME_RATE = 30

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()


player = pygame.Rect(50, 50, 50, 50)  # x, y, width, height

BOARD.fill((0, 0, 0))
pygame.draw.rect(BOARD, (255, 0, 0), player)

pygame.display.flip()
CLOCK.tick(FRAME_RATE)

input('Press [enter] to end.')

pygame.quit()
