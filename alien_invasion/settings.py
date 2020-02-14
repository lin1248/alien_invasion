from color import Bullets_Color as bc

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ship_speed = 1.5
        self.ship_limit = 3
        
        self.alien_speed = 1
        self.alien_drop_speed = 10
        # 1表示向左，-1表示向右
        self.fleet_direction = 1
        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = bc.Red
        self.bullet_allowed = 5
        self.fire_cold_time = 33
