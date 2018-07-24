import sys
import pygame
from bullet import Bullet

# 将项目中的主要函数都放到这边进行重构，简化代码，使逻辑清晰
def check_events(ai_settings, screen, ship, bullets):
	# 1、监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# 6、每当按下键盘会注册一个事件
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
			# # 6、如果是向右，则更新飞船在x轴的位置
			# if event.key == pygame.K_RIGHT:
			# 	ship.moving_right = True
			# 	# 向右移动飞船
			# 	# 7、现在这边通过改变移动标志的开关来决定移动并实现持续的移动
			# 	# ship.rect.centerx += 1
			# # 8、实现向左移动
			# elif event.key == pygame.K_LEFT:
			# 	ship.moving_left = True

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			# if event.key == pygame.K_RIGHT:
			# 	ship.moving_right = False
			# # 8、实现向左移动
			# elif event.key == pygame.K_LEFT:
			# 	ship.moving_left = False
# 11、重构check_events
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	# 6、如果是向右，则更新飞船在x轴的位置
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	# 向右移动飞船
	# 7、现在这边通过改变移动标志的开关来决定移动并实现持续的移动
	# ship.rect.centerx += 1
	# 8、实现向左移动
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
		# # 16、限制子弹的数量
		# if len(bullets) < ai_settings.bullets_allowed:
		# 	# 14、创建一颗子弹并将其加入到编组bullets中
		# 	new_bullet = Bullet(ai_settings, screen, ship)
		# 	bullets.add(new_bullet)
	# 19、添加q键从而实现游戏的退出
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	# 8、实现向左移动
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
	"""更像屏幕上的图像并切换到新屏幕"""
	# 2、每次循环都重绘屏幕，这个方法只接受颜色这个参数
	# screen.fill(bg_coclor)
	screen.fill(ai_settings.bg_color)

	# 14、在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	# 4、绘制飞船
	ship.blitme()

	# 1、显示最近绘制的屏幕
	pygame.display.flip()

# 17 重构主程序里的代码，将函数移到这边
def update_bullets(bullets):
	"""更新子弹的位置并删除已消失的子弹"""
	# 13、更新子弹的位置
	bullets.update()

	# 15、删除已消失的子弹, !!!因为此次循环中bullets已发生变化，所以我们要遍历此次的副本，
	# 注意点！！！：而不能在原来的编组中遍历。想想既要遍历它，又要改变它，这两者是矛盾的。
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	# print(len(bullets))

# 18、移动发射子弹的代码，使check_keydown_events尽量简单
def fire_bullet(ai_settings, screen, ship, bullets):
	"""如果还没有达到限制就发射一颗子弹"""
	# 16、限制子弹的数量
	if len(bullets) < ai_settings.bullets_allowed:
		# 14、创建一颗子弹并将其加入到编组bullets中
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
