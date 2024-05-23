import pygame
  
# 定义一个按钮类  
class Button:  
    def __init__(self, window, text, x, y, width, height, btn_color, btn_frm_color, btn_frm_change_color):  
        self.window = window  
        self.text = text  
        self.x = x  
        self.y = y  
        self.width = width  
        self.height = height  
        self.btn_color = btn_color  
        self.btn_frm_color = btn_frm_color
        self.btn_frm_change_color = btn_frm_change_color  
        self.rect = pygame.Rect(x, y, width, height)  
        self.font = pygame.font.SysFont("simhei", 16)  # 使用系统默认字体和指定大小  
  
    def draw(self):  
        # 根据鼠标位置设置颜色  
        if self.rect.collidepoint(pygame.mouse.get_pos()):  # 检测一个点是否包含在该 Rect 对象中
            pygame.draw.rect(self.window, self.btn_color, self.rect) 
            pygame.draw.rect(self.window, self.btn_frm_change_color, self.rect, 2)   
        else:  
            pygame.draw.rect(self.window, self.btn_color, self.rect)  
            pygame.draw.rect(self.window, self.btn_frm_color, self.rect, 2)  
  
        # 在按钮上居中绘制文本  
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # 文本颜色为黑色 
        text_rect = text_surface.get_rect(center=self.rect.center)  
        self.window.blit(text_surface, text_rect)  
  
    def handle_event(self, event):  
        # 检查鼠标点击事件  
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if self.rect.collidepoint(pygame.mouse.get_pos()):  
                print(f"Button '{self.text}' clicked!")  
  
  
# 初始化pygame  
# pygame.init()  
# window = pygame.display.set_mode((800, 600))  
# pygame.display.set_caption("Pygame Button Example")  
  
# # 创建按钮实例  
# button = Button(window, "Click Me!", 100, 100, 200, 50, (220, 190, 74), (164, 136, 83))  
  
# # 游戏主循环  
# running = True  
# while running:  
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT:  
#             running = False  
#         button.handle_event(event)  
  
#     window.fill((0, 0, 0))  # 假设背景色为黑色  
#     button.draw()  
#     pygame.display.flip()  
  
# pygame.quit()  
# sys.exit()