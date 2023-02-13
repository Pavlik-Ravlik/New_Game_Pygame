import pygame
import controls
from player import Player


def run():
    pygame.init()
    screen = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption('Стрелялка')
    bg_color = (0, 0, 0)
    player = Player(screen)

    while True:
        controls.events(player)
        player.update_player()
        controls.update(bg_color, screen, player)


run()
