import pygame


class Player():

    def __init__(self, screen):  # инициализация игрока
        self.screen = screen
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def autput():  # рисование пушки
        self.screen.blit(self.image, self.rect)
