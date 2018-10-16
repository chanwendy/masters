import pygame


class Ship():

    def __init__(self, screen,):

        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.center=float(self.rect.centerx)
    def updatemo(self):
        if self.moving_right:
            self.center += 1
        if self.moving_left:
            self.center -= 1
        self.rect.centerx=self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        self.center=self.screen_rect.centerx