import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		# 重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True
		# 重置记分牌图像
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()

		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人，并让飞船居中
		creat_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()	

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	"""响应松开"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
	"""更像屏幕上的图像并切换到新屏幕"""
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	# 显示得分
	sb.show_score()

	# 如果游戏处于非活动状态就绘制按钮
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""更新子弹的位置并删除已消失的子弹"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""响应子弹和外星人的碰撞"""
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		stats.level += 1
		sb.prep_level()

		creat_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
	"""如果还没有达到限制就发射一颗子弹"""
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def creat_fleet(ai_settings, screen, ship, aliens):
	"""创建外星人群"""
	alien = Alien(ai_settings, screen)
	# 通过这个创建的外星人来获取外星人的rect的宽度和高度，并用来计算一行可放置几个外星人
	alien_width = alien.rect.width
	number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
		
def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可容纳多少个机器人"""
	avaliable_space_x = ai_settings.screen_width - 2*alien_width
	number_aliens_x = int(avaliable_space_x / (2*alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	# 创建一个外星人并加入当前行
	alien = Alien(ai_settings, screen)
	alien.x = alien.rect.width + 2*alien.rect.width*alien_number
	alien.rect.x = alien.x
	alien.y = alien.rect.height + 2*alien.rect.height*row_number
	alien.rect.y = alien.y
	
	aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
	"""计算可容纳多少外星人"""
	avaliable_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(avaliable_space_y / (2*alien_height))
	return number_rows

def update_alines(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""检查是否有外星人处于边缘并更新外星人群中所以外星人的位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	# 检查外星人与飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
	# 检查是否有外星人到达屏幕底部
	check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
	"""外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""将整群外星人向下移并改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	if stats.ships_left > 0:
		stats.ships_left -= 1
		sb.prep_ships()

		# 清空外星人及子弹列表——>重新开始
		aliens.empty()
		bullets.empty()

		# 创建一群新的外星人，并将飞船放到屏幕底部中央
		creat_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		# 暂停
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
	"""检查是否有外星人到达了屏幕底部"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# 像飞船被撞到一样处理
			ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
			break

def check_high_score(stats, sb):
	"""检查是否是新的最高得分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
