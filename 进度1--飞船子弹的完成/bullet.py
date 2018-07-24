import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""12、一个对飞船发射的子弹进行管理的类"""
	# 通过使用sprite可将游戏中相关元素编组，进而同时操作编组中的所有元素
	def __init__(self, ai_settings, screen, ship):
		"""在飞船所处位置创建一个子弹对象"""
		super(Bullet, self).__init__()
		self.screen = screen

		# 先在（0，0）创建子弹，在设置子弹的正确位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# 用小数存储子弹在y轴的位置
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""向上移动子弹"""
		# 更新表示子弹位置的小数值
		self.y -= self.speed_factor
		# 更新表示子弹的rect的位置
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect) 

		