import pygame
# import sys
from settings import Settings 
from ship import Ship 
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# 1、初始化一个屏幕对象
	pygame.init()

	# 3、参数设置统一存放到settings模块中
	ai_settings = Settings()
	# 1、设置窗口的大小
	# screen = pygame.display.set_mode((1200, 800))
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	# 1、设置窗口的名字
	pygame.display.set_caption("Alien Invasion")

	# 4、创建一艘飞船
	ship = Ship(ai_settings ,screen)
	# 13、创建一个用于存储子弹的编组，Group类似列表但提供了有利于游戏编程的一些功能
	bullets = Group()

	# 2、pygame默认的背景颜色为黑色，这边设置成其他颜色
	# bg_color = (230, 230, 230)

	# 1、开始游戏的主循环
	while True:
		# # 1、监听键盘和鼠标事件
		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		# 5、重构，将主要的函数放到game_function模块中
		# gf.check_events()
		# 6、每当按下键盘，更新飞船在x轴的位置
		# gf.check_events(ship)
		# 13、对子弹的处理，填充子弹到数组bullets中
		gf.check_events(ai_settings, screen, ship, bullets)
		# 7、实现飞船的持续移动
		ship.update()
		
		# # 13、对子弹的处理
		# bullets.update()

		# # 15、删除已消失的子弹, !!!因为此次循环中bullets已发生变化，所以我们要遍历此次的副本，
		# # 注意点！！！：而不能在原来的编组中遍历。想想既要遍历它，又要改变它，这两者是矛盾的。
		# for bullet in bullets.copy():
		# 	if bullet.rect.bottom <= 0:
		# 		bullets.remove(bullet)
		# print(len(bullets))
		# 17、移到gf模块中
		gf.update_bullets(bullets)

		# # 2、每次循环都重绘屏幕，这个方法只接受颜色这个参数
		# # screen.fill(bg_coclor)
		# screen.fill(ai_settings.bg_color)

		# # 4、绘制飞船
		# ship.blitme()

		# # 1、显示最近绘制的屏幕
		# pygame.display.flip()
		# 5、重构，将主要的函数放到game_function模块中
		# gf.update_screen(ai_settings, screen, ship)
		# 13、对子弹的处理
		gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
