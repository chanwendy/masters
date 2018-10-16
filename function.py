import sys
import pygame
from setting import Setting,Word
from ship import  Ship
from bullet import  Bullet
from master import  Master
from time import sleep

def check_events(m_setting,screen,stats,play_button,ship,masters,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, m_setting, screen, ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play(m_setting,screen,stats,play_button,ship,masters,bullets,mouse_x,mouse_y)
def check_play(m_setting,screen,stats,play_button,ship,masters,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_stats()
        stats.game_active=True
        masters.empty()
        bullets.empty()
        creat_master(m_setting,screen,ship,masters)
        ship.center_ship()

def check_keydown_events(event, m_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key== pygame.K_SPACE:
        new_bullet=Bullet(m_setting,screen,ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update(m_setting,screen,ship,bullets,masters,play_button,stats):
    screen.fill(m_setting.bg_color)  # setting bg
    ship.blitme()
    masters.draw(screen)
    if not stats.game_active:

        play_button.draw_button()
    for bullet in bullets.sprites():
        bullet.bullet_draw()



def bullet_up(m_setting,screen,ship,masters,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,masters,True,True)
    if len(masters)==0:
        bullets.empty()
        creat_master(m_setting,screen,ship,masters)
def creat_master(m_setting,screen,ship,masters):
    ship=Ship(screen)
    master=Master(m_setting,screen)
    ship_height=ship.rect.height
    master_width=master.rect.width
    master_height=master.rect.height
    avaliable_x=m_setting.screen_width-2*master_width
    avaliable_y=m_setting.screen_length-3*master_height-ship_height
    number_x=avaliable_x/(2*master_width)
    number_y=int(avaliable_y/(2*master_height))
    for master_y in  range(number_y):
        for master_nmber in range(int(number_x)):
            master=Master(m_setting,screen)
            master.x = master_width+2*master_width*master_nmber
            master.y= master_height+2*master.rect.height*master_y
            master.rect.x=master.x
            master.rect.y=master.y
            masters.add(master)
def update_mon(m_setting, stats, screen, ship, masters, bullets):
    check_master(m_setting,masters)
    masters.update()
    if pygame.sprite.spritecollideany(ship,masters):
        ship_hit(m_setting, stats, screen, ship, masters, bullets)
def check_master(m_setting,masters):
    for master in masters.sprites():
        if master.check_edge():
            change_direction(m_setting,masters)
            break
def change_direction(m_setting,masters):
    for master in masters.sprites():
        master.rect.y+=m_setting.master_speed
    m_setting.master_dire*=-1


def ship_hit(m_setting, stats, screen, ship, masters, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
    masters.empty()
    bullets.empty()
    creat_master(m_setting, screen, ship, masters)
    ship.center_ship()
    sleep(0.5)