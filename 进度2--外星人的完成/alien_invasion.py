import pygame
from settings import Settings
from game_stats import GameStats 
from ship import Ship 
# from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 6、创建用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	
	ship = Ship(ai_settings ,screen)
	bullets = Group()

	# # 1、创建一个外星人
	# alien = Alien(ai_settings, screen)
	# 2、创建一群外星人
	aliens = Group()
	gf.creat_fleet(ai_settings, screen, ship, aliens)

	while True:
		# 需要玩家按q退出或者点击等，所以要不断运行
		gf.check_events(ai_settings, screen, ship, bullets)

		# 8、增加游戏结束
		if stats.game_active:
			ship.update()
			# 4、可以射杀外星人，一行代码解决，调用了pygame编组的一个方法，🐮
			# 5、当此轮的外星人全部被射杀后出现新的外星人
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			# 3、移动外星人
			# 7、外星人与飞船相撞或着外星人到达屏幕底部
			gf.update_alines(ai_settings, stats, screen, ship, aliens, bullets)
		# gf.update_screen(ai_settings, screen, ship, alien, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
