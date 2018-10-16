import  pygame
class Setting():
    def __init__(self):
        self.screen_width=1000
        self.screen_length=800
        self.bg_color=(230,230,230)
        self.bullet_v=3
        self.bullet_width=10
        self.bullet_height=30
        self.bullet_color=(60,60,60)
        self.master_v=3
        self.master_speed=20
        self.master_dire=1
        self.ship_limit=3
class Word():
    def __init__(self,screen):
        self.screen=screen
        self.front=pygame.font.SysFont('START',100)
        self.textobj=self.front.render('START',1,(0,0,255))
        self.textrect=self.textobj.get_rect()
        self.screen_rect = screen.get_rect()
        self.textrect.center=self.screen_rect.center

    def dis(self):
        self.screen.blit(self.textobj,self.textrect)