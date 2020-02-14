
import sys
import pygame
import settings 
import ship 
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats

def run_game():
    _settings = settings.Settings()

    width = _settings.screen_width
    height = _settings.screen_height
    #初始化游戏并创建一个屏幕对象
    pygame.init()

    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Alien Invasion")

    """创建一个用于存储游戏统计信息的实例"""
    stats = GameStats(_settings)

    #设置背景色
    bg_color = _settings.bg_color

    #创建一艘飞船
    _ship = ship.Ship(screen,_settings)

    bullets = Group()
    aliens = Group()
    gf.create_fleet(_settings,screen,_ship,aliens)
    
    #开始游戏主循环
    while True:
        gf.check_events(_settings,screen,_ship,bullets)
        
        gf.update_screen(_settings,stats,screen,_ship,aliens,bullets)
        

run_game()