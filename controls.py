import pygame
import sys


def events(player):  # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.mright = True
            elif event.key == pygame.K_a:
                player.mleft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.mright = False
            elif event.key == pygame.K_a:
                player.mleft = False


def update(bg_color, screen, player):  # обновление екрана
    screen.fill(bg_color)
    player.autput()
    pygame.display.flip()
