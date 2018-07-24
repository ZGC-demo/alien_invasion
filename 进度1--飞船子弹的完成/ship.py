import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 9、 调整飞船的移动速度
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # 将对实际图形的处理转为对矩形的处理，这边是图形的矩形
        self.rect = self.image.get_rect()
        # 这边是显示屏幕的矩形
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        # 通过设置矩形的参数使图像居中，如center——屏幕正中央、centerx——x轴中央、centery——y轴中央
        self.rect.centerx = self.screen_rect.centerx
        # 让游戏元素与屏幕边缘对齐，如top、bottom、left、right
        self.rect.bottom = self.screen_rect.bottom

        # 9、在飞船的属性center中存储小数值, 因为rect只支持整数，所以要转为小数
        self.center = float(self.rect.centerx)

        # 7、移动标志
        self.moving_right = False
        # 8、实现向左移动，同理
        self.moving_left = False

    def update(self):
    	"""7、根据移动标志调整飞船位置"""
    	# 9、更新飞船的center值，而不是rect
        # 10、通过屏幕的距离来限制飞船的移动范围
    	if self.moving_right and self.rect.right < self.screen_rect.right:
    		# self.rect.centerx += 1
    		self.center += self.ai_settings.ship_speed_factor
    	# 10、通过屏幕的距离来限制飞船的移动范围, self.screen_rect.left==0
    	if self.moving_left and self.rect.left > self.screen_rect.left:
    		# self.rect.centerx -=1
    		self.center -= self.ai_settings.ship_speed_factor
    	# 9、根据self.center更新rect对象
    	self.rect.centerx = self.center


    def blitme(self):
        """在指定位置绘制飞船"""
        # 将图像self.image绘制到self.rect
        self.screen.blit(self.image, self.rect)
