import sys
import pygame
from bullet import Bullet

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

def update_screen(_settings,screen,_ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环都会重回屏幕
    screen.fill(_settings.bg_color)
    
        
    #显示飞船
    _ship.update(_settings,screen,_ship,bullets)
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    _ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()
