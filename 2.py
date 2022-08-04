#!/usr/bin/env python3
"""A simple skiing game.

Day-iteration:
2-1: Screen with stationary rectangle
2-2: Game loop and movement
"""
import pygame


BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 480, 640
FRAME_RATE = 30
BOARD_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_X = BOARD_WIDTH // 2
PLAYER_Y = BOARD_HEIGHT // 2

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()


player = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

game_on = True
while game_on:
    BOARD.fill(BOARD_COLOR)
    pygame.draw.rect(BOARD, PLAYER_COLOR, player)
    player.x += 1
    player.y += 1
    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

    if player.y > 500:
        game_on = False

pygame.quit()
