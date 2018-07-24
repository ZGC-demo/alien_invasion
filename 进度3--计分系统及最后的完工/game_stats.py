class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self, ai_settings):
		"""初始化统计信息"""
		self.ai_settings = ai_settings
		self.reset_stats() # 相当于该函数里面的内容都在初始化里面，可直接调用

		# # 游戏刚启动时处于活动状态
		# self.game_active = True
		# 让游戏一开始处于非活跃状态，用play按钮触发开始
		self.game_active = False

		# 因为在任何情况下都不会重置最高得分，所以放在这边
		self.high_score = 0

	def reset_stats(self):
		"""初始化在游戏运行期间间可能变化的统计信息"""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		# 17、显示等级
		self.level = 1
		