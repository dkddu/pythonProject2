import pygame.font
from ship import Ship
from  pygame.sprite import Group

class Scoreboard:
    """显示信息的类"""

    def __init__(self,ai_game):
        """初始化得分涉及的属性"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game
        #字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.ships = pygame.sprite.Group()

        #准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        """显示剩余的飞船"""
        self.ships.empty()
        for ship_number in  range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 20 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)
    def prep_level(self):
        """将等级转换为渲染的图像"""
        level_str = str(self.stats.level)
        self.level_images = self.font.render(level_str,True,self.text_color,self.settings.bm_color)
        #放在得分下方
        self.level_rect = self.level_images.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.high_score_rect.bottom + 20
    def prep_high_score(self):
        high_score = round(self.stats.score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bu_color)
        #将最高分显示在屏幕左上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 40
        self.high_score_rect.top = 60

    def check_high_score(self):
        """检查是否诞生了最高得分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def prep_score(self):
        #得分字体
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        #分数显示位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_images,self.level_rect)
        self.ships.draw(self.screen)