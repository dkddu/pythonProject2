class Settings:
    """储存游戏《外星人在地球》中设置的所有类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width= 1200
        self.screen_height= 800
        self.bg_color = (230, 230, 230)
        self.bu_color = (0,229,238)
        self.bm_color = (255,250,205)
        #飞船速度
        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 30
        #外星人设置
        self.fleet_drop_speed = 5
        #加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏进行变化的设置"""
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.bullet_speed = 3
        # fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        #记分
        self.alien_points = 50
        self.score_scale = 1.5

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)

    def set_difficulty(self, difficulty_level):
        if difficulty_level == 'easy':
            # 调整易难度的设置
            self.ship_speed = 2.0
            self.bullet_speed = 3.5
            self.alien_speed = 1.0
        elif difficulty_level == 'medium':
            # 调整中等难度的设置
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.5
        elif difficulty_level == 'hard':
            # 调整困难难度的设置
            self.ship_speed = 1.0
            self.bullet_speed = 2.5
            self.alien_speed = 2.0
