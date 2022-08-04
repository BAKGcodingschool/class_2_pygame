#!/usr/bin/env python3
"""A simple skiing game.

Day-iteration:
2-1: Screen with stationary rectangle
2-2: Game loop and movement
2-3: User input
2-4: KEYUP for smoother movement
2-5: Board boundaries and name == main
extra: control two squares

Questions:
1. Why does one box always overlap the other?
    a. How would you change the code so that the other box is on top?

"""
import pygame


BOARD_SIZE = BOARD_WIDTH, BOARD_HEIGHT = 480, 640
FRAME_RATE = 30
BOARD_COLOR = (0, 0, 0)
P1_SPEED = P2_SPEED = 5

P1_COLOR = (255, 0, 0)
P1_WIDTH = P1_HEIGHT = 50
P1_X = (BOARD_WIDTH - P1_WIDTH) // 2
P1_Y = (BOARD_HEIGHT - P1_HEIGHT) * 3 // 4

P2_COLOR = (0, 0, 255)
P2_WIDTH = P2_HEIGHT = 50
P2_X = (BOARD_WIDTH - P2_WIDTH) // 2
P2_Y = (BOARD_HEIGHT - P2_HEIGHT) // 4


def main():
    """Does the work.
    """
    p1 = pygame.Rect(P1_X, P1_Y, P1_WIDTH, P1_HEIGHT)
    p1_x_inc = p1_y_inc = 0

    p2 = pygame.Rect(P2_X, P2_Y, P2_WIDTH, P2_HEIGHT)
    p2_x_inc = p2_y_inc = 0

    game_on = True
    while game_on:
        BOARD.fill(BOARD_COLOR)
        pygame.draw.rect(BOARD, P1_COLOR, p1)
        pygame.draw.rect(BOARD, P2_COLOR, p2)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_on = False

                elif event.key == pygame.K_LEFT:
                    p1_x_inc = -P1_SPEED
                elif event.key == pygame.K_RIGHT:
                    p1_x_inc = P1_SPEED
                elif event.key == pygame.K_UP:
                    p1_y_inc = -P1_SPEED
                elif event.key == pygame.K_DOWN:
                    p1_y_inc = P1_SPEED

                elif event.key == pygame.K_a:
                    p2_x_inc = -P2_SPEED
                elif event.key == pygame.K_d:
                    p2_x_inc = P2_SPEED
                elif event.key == pygame.K_w:
                    p2_y_inc = -P2_SPEED
                elif event.key == pygame.K_s:
                    p2_y_inc = P2_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    p1_x_inc = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    p1_y_inc = 0

                if event.key in (pygame.K_a, pygame.K_d):
                    p2_x_inc = 0
                elif event.key in (pygame.K_w, pygame.K_s):
                    p2_y_inc = 0

        p1.x += p1_x_inc
        p1.y += p1_y_inc

        p2.x += p2_x_inc
        p2.y += p2_y_inc

        if p1.x < 0:
            p1.x = 0
        elif p1.x > BOARD_WIDTH - p1.width:
            p1.x = BOARD_WIDTH - p1.width
        if p1.y < 0:
            p1.y = 0
        elif p1.y > BOARD_HEIGHT - p1.height:
            p1.y = BOARD_HEIGHT - p1.height

        if p2.x < 0:
            p2.x = 0
        elif p2.x > BOARD_WIDTH - p2.width:
            p2.x = BOARD_WIDTH - p2.width
        if p2.y < 0:
            p2.y = 0
        elif p2.y > BOARD_HEIGHT - p2.height:
            p2.y = BOARD_HEIGHT - p2.height

        pygame.display.flip()
        CLOCK.tick(FRAME_RATE)


if __name__ == '__main__':
    pygame.init()
    BOARD = pygame.display.set_mode(BOARD_SIZE)
    CLOCK = pygame.time.Clock()
    main()
    pygame.quit()
