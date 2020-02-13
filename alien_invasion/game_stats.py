class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,_settings):
        """初始化统计信息"""
        self._settings = _settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏中可能变化的统计数据"""
        self.ships_left = self._settings.ship_limit
