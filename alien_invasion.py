import sys
from time import  sleep

import pygame

from settings import Settings
from  game_stats import Gamestats
from  button import Button
from ship import Ship
from  scoreboard import  Scoreboard
from bullet import  Bullet
from alien import  Alien
class   AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings=Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.background_image = pygame.image.load("images/backgroud.bmp").convert()
        self.background_image = pygame.transform.scale(self.background_image, (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        #创建一个用于统计游戏数据的实例库
        self.stats = Gamestats(self)
        self.sb = Scoreboard(self)
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #创建按钮
        self.play_button = Button(self,"高远打飞机",400)
        self.easy_button = Button(self, "简单模式", 100)
        self.medium_button = Button(self, "中等模式", 200)
        self.hard_button = Button(self, "困难模式", 300)
    def run_game(self):
        """开始游戏的主循环"""

        while True:
            self._check_events()
            if self.stats.game_active :
                self._update_screen()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_aliens_bottom()
            self._update_screen()
            # 监视键盘和鼠标事件
    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    def _check_play_button(self,mouse_pos):
        """在玩家单机play时开始那个游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.stats.game_active == False:
            self._start_game()
        if self.easy_button.rect.collidepoint(mouse_pos):
            self._start_game()
            self.settings.set_difficulty("easy")
        elif self.medium_button.rect.collidepoint(mouse_pos):
            self._start_game()
            self.settings.set_difficulty("medium")
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self._start_game()
            self.settings.set_difficulty("hard")

    def _start_game(self):
        # 重置游戏信息
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_level()
        self.sb.prep_score()
        self.sb.prep_ships()
        # 清空余下的外星人和子弹
        self.aliens.empty()
        self.bullets.empty()
        # 创建一群新的外星人并让飞船飞在空中
        self._create_fleet()
        self.ship.center_ship()
        # 影藏鼠标光标
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_0 and self.stats.game_active == False:
            self._start_game()
        elif event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down =True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹位置并删除消失的子弹"""
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
            #检查是否有子弹击中了外星人
            #如果是，就删除相应的自弹和外星人
    def _check_bullet_alien_collisions(self):
        """相应子弹和外星人碰撞"""
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens, True, True)
        if not self.aliens:
            #删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            #提高等级
            self.stats.level +=1
            self.sb.prep_level()
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.prep_high_score()


    def _create_fleet(self):
        """创建外星人群"""
        #创建一个外星人并计算一行可容纳多少外星人
        #外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_alien_x = available_space_x // (2 * alien_width)
        #计算屏幕可容纳多少外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 3 * alien_height - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        #创建第一行外星人
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number,row_number)
    def _create_alien(self,alien_number,row_number):
        """创建一个外星人并将其加入当前行"""
        alien =Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width +2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """检查是否有外星人位于屏幕边沿，更新外星人群众所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        #检测外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """响应飞船被外星人撞到"""
        if self.stats.ships_left > 0:
            #将shipleft减1
            self.stats.ships_left -=1
            self.sb.prep_ships()
            #清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            #创建一群新的外星人，并将飞船放到屏幕底部的中央
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #像飞船被撞到一样处理
                self._ship_hit()
                break
    def _check_fleet_edges(self):
        """有外星人到达边缘时采取的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """将外星人下移,并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.blit(self.background_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        #如果游戏处于非活跃状态，就显示play按钮
        if self.stats.game_active == False:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        pygame.display.flip()
if __name__ == '__main__':
    ##创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
    # 在Python程序中，if __name__ == '__main__': main()
    # 是一个常见的结构，用于确保当脚本直接运行（而不是被其他脚本导入作为模块使用时），才会执行特定的代码块。
    #
    # 这里的
    # main()
    # 函数通常包含了整个程序的主要逻辑和入口点。当你直接运行这个脚本文件时，Python解释器会自动设置特殊变量
    # __name__
    # 为字符串
    # '__main__'。
    #
    # 所以这段代码的意义是：如果当前模块（也就是包含这段代码的脚本）是作为主模块被执行（即它不是被其他模块导入的情况），那么就调用
    # main()
    # 函数来启动程序。
    #
    # 这样做有助于组织代码，使一些函数或类可以被外部模块复用，同时确保主要执行流程只在该脚本作为独立程序运行时启动。