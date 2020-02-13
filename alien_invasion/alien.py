import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,_settings,screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.settings = _settings
        self.screen = screen

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()

        # 是每个外星人最初都在屏幕左上方
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """向右移动外星人"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            print("到达边界右")
            return True
        elif self.rect.left <= 0:
            print("到达边界左")
            return True