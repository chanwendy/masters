import pygame
from pygame.sprite import Sprite
from setting import Setting
from ship import  Ship
m_setting=Setting()
screen = pygame.display.set_mode((m_setting.screen_width, m_setting.screen_length))
class Bullet(Sprite):
    ship = Ship(screen)
    def __init__(self,m_setting,screen,ship):
        super().__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,m_setting.bullet_width,m_setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=m_setting.bullet_color
        self.speed=m_setting.bullet_v

    def update(self, *args):
        self.y -=m_setting.bullet_v
        self.rect.y=self.y

    def bullet_draw(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
