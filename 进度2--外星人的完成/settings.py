class Settings():
	def __init__(self):
		"""初始化游戏的设置"""
		# 屏幕的设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# 飞船的设置
		self.ship_speed_factor = 1.5 # 飞船速度
		self.ship_limit = 3 # 飞船数量

		# 子弹设置
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# 外星人设置
		self.alien_speed_factor = 1
		# 当有外星人撞击墙壁时，外星人向下移动的速度
		self.fleet_drop_speed = 100
		# self.fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1