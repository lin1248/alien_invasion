import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对飞船发射的子弹的设置"""

    def __init__(self,_settings,screen,_ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,_settings.bullet_width,
                                _settings.bullet_height)
        self.rect.centerx = _ship.rect.centerx
        self.rect.top = _ship.rect.top

        self.y = float(_ship.rect.y)

        self.color = _settings.bullet_color
        self.speed = _settings.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
