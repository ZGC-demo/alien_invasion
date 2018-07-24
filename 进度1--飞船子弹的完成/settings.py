class Settings():
	"""3、存储整个项目的所有设置，就是将项目中的一些可变的，可调整的参数存放到这边，方便统一更改"""

	def __init__(self):
		"""初始化游戏的设置"""
		# 3、屏幕的设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# 飞船的设置
		# 9、速度，即移动的距离
		self.ship_speed_factor = 1.5

		# 12、子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3