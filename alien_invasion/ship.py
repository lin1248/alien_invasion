import pygame
from bullet import Bullet

class Ship():
    count = 0
    
    def __init__(self,screen,_settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.settings = _settings
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False
        self.count = 0
        self.fire_cold_time = self.settings.fire_cold_time
        

    def update(self,_settings,screen,_ship,bullets):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center_x -= self.settings.ship_speed
        elif self.moving_up and self.rect.top > 0 :
            self.center_y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.settings.ship_speed
        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y
        if self.fire and self.count == self.fire_cold_time:
            self.count = 0
            if len(bullets) < _settings.bullet_allowed:
                new_bullet = Bullet(_settings,screen,_ship)
                bullets.add(new_bullet)
                print("new bullet")
        elif self.fire and self.count < self.fire_cold_time:
            self.count += 1
            print(self.count)
        elif self.fire and self.count > self.fire_cold_time:
            self.count = 0
            

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
