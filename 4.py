#!/usr/bin/env python3
"""A simple skiing game.

Day-iteration:
2-1: Screen with stationary rectangle
2-2: Game loop and movement
2-3: User input
2-4: KEYUP for smoother movement
"""
import pygame


BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 480, 640
FRAME_RATE = 30
BOARD_COLOR = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
PLAYER_WIDTH = PLAYER_HEIGHT = 50
PLAYER_X = (BOARD_WIDTH - PLAYER_WIDTH) // 2
PLAYER_Y = (BOARD_HEIGHT - PLAYER_HEIGHT) // 2
PLAYER_SPEED = 5

pygame.init()

BOARD = pygame.display.set_mode(BOARD_SIZE)
CLOCK = pygame.time.Clock()


player = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
player_x_inc = player_y_inc = 0

game_on = True
while game_on:
    BOARD.fill(BOARD_COLOR)
    pygame.draw.rect(BOARD, PLAYER_COLOR, player)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_on = False
            elif event.key == pygame.K_LEFT:
                player_x_inc = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player_x_inc = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                player_y_inc = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                player_y_inc = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_inc = 0
            elif event.key == pygame.K_RIGHT:
                player_x_inc = 0
            elif event.key == pygame.K_UP:
                player_y_inc = 0
            elif event.key == pygame.K_DOWN:
                player_y_inc = 0

    player.x += player_x_inc
    player.y += player_y_inc

    pygame.display.flip()
    CLOCK.tick(FRAME_RATE)

pygame.quit()
