import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(_settings,screen,_ship,bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                _ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                _ship.moving_left = True
            elif event.key == pygame.K_UP:
                _ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                _ship.moving_down = True
            elif event.key == pygame.K_SPACE:
                _ship.fire = True
            elif event.key == pygame.K_q:
                sys.exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                _ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                _ship.moving_left = False
            elif event.key == pygame.K_UP:
                _ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                _ship.moving_down = False
            elif event.key ==pygame.K_SPACE:
                _ship.fire = False

def update_screen(_settings,screen,_ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重回屏幕
    screen.fill(_settings.bg_color)
    
        
    #显示飞船
    _ship.update(_settings,screen,_ship,bullets)
    bullets.update()
    check_fleet_edges(_settings,aliens)
    aliens.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(_settings,screen,_ship,aliens,bullets)
    #print(len(bullets))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    _ship.blitme()
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    pygame.display.flip()

#检查子弹与飞船是否接触
def check_bullet_alien_collisions(_settings,screen,_ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    #如果外星人都消失，就新建一群外星人  
    if len(aliens)==0:
        bullets.empty()
        create_fleet(_settings,screen,_ship,aliens)

def create_fleet(_settings,screen,ship,aliens):
    """创建外星人的群"""
    alien = Alien(_settings,screen)
    num_aliens_x = get_number_aliens_x(_settings,alien.rect.width)
    num_aliens_rows = get_number_rows(_settings,ship.rect.height,alien.rect.height)
    # 创建第一群外星人
    for row_number in range(num_aliens_rows):
        for alien_number in range(num_aliens_x):
            create_alien(_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(_settings,alien_width):
    """计算每行可以容纳多少外星人"""
    available_space_x = _settings.screen_width - 2 * alien_width
    num_aliens_x = int(available_space_x / (2 * alien_width))
    return num_aliens_x

def create_alien(_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人放在当前行"""
    alien = Alien(_settings,screen)
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(_settings,ship_height,alien_height):
    """计算可以容纳多少行外星人"""
    available_space_y = (_settings.screen_height - 
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            print("到达边界")
            change_fleet_direction(settings,aliens)
            break

def change_fleet_direction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    settings.fleet_direction *= -1

#def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullet):
 #   """检查是否有外星人到达屏幕底端"""
#    screen_rect = screen.get_rect()
#    for alien in aliens.sprites():
#        if alien.rect.bottom >= screen_rect.bottom:
#            # 像飞船被撞到一样处理
#            ship_hit(ai_settings,)"""