import  pygame
from pygame.sprite import Sprite
class Master(Sprite):
    def __init__(self,m_setting,screen):
        super().__init__()
        self.screen=screen
        self.m_setting=m_setting
        self.image=pygame.image.load('images/master.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
    def biltms(self):
        self.screen.blit(self.image,self.rect)
    def update(self, *args):
        self.x += (self.m_setting.master_v*self.m_setting.master_dire)
        self.rect.x=self.x
    def check_edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return  True
