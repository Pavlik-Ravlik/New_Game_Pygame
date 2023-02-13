import pygame
import sys


class Player():

    def __init__(self, screen):  # инициализация игрока
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(
            'Player_png/player(1).png').convert_alpha(), (100, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def autput(self):  # рисование игрока
        self.screen.blit(self.image, self.rect)

    def update_player(self):  # Обновление позиции игрока
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
