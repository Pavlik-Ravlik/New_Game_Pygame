import pygame
import sys
from player import Player


def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Стрелялка')
    bg_color = (0, 0, 0)
    player = Player(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT
            sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()


run()
