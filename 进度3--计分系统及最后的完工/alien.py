import pygame
from pygame.sprite import Sprite

# 进度1刚才忘记继承Sprite类了，所以导致老是报错，alien是Alien对象不能add，，，
class Alien(Sprite):
	"""初始化外星人并设置其起始位置"""
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		# 加载外星人图像，并设置其rect属性
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# 每个外星人最初都在左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储外星人的准确位置
		self.x = float(self.rect.x)

	def blitme(self):
		"""在指定位置绘制外星人"""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""如果外星人撞击了墙壁就返回True"""
		screen_rect = self.screen.get_rect()
		if self.rect.right > screen_rect.right:
			return True
		elif self.rect.left < screen_rect.left:
			return True

	def update(self):
		"""向左或向右移动外星人"""
		# fleet_direction值为1或-1，1即为右移，-1即为左移
		self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
		self.rect.x = self.x
		