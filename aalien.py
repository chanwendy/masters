import pygame
from button import Button
from setting import Setting,Word
from ship import  Ship
import  function as fn
from pygame.sprite import Group
from master import Master
from gamestate import GameStats

def run_game():
    pygame.init()
    m_setting=Setting()
    screen=pygame.display.set_mode((m_setting.screen_width,m_setting.screen_length))
    ship = Ship(screen)
    i_word=Word(screen)
    bullets=Group()
    stats=GameStats(m_setting)
    masters=Group()
    master=Master(m_setting,screen)
    fn.creat_master(m_setting, screen, ship,masters)
    play_button=Button(m_setting,screen,'PLAY')
    pygame.display.set_caption('Hello Game')
    while True:
        fn.check_events(m_setting,screen,stats,play_button,ship,masters,bullets)
        if stats.game_active:
            ship.updatemo()
            fn.bullet_up(m_setting,screen,ship,masters,bullets)
            fn.update_mon(m_setting, stats, screen, ship, masters, bullets)
        fn.update(m_setting, screen, ship, bullets, masters, play_button,stats)
        pygame.display.flip()
run_game()


