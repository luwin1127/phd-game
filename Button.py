import pygame
  
class Button: 
    '''定义按钮类 '''
    def __init__(self, window, text, x, y, width, height):  
        self.window = window  
        self.text = text  
        self.x = x  
        self.y = y  
        self.width = width  
        self.height = height
        self.btn_color = (245, 222, 179)  
        self.btn_frm_color = (220, 190, 74)
        self.btn_frm_change_color = (164, 136, 83)  
        self.rect = pygame.Rect(x, y, width, height)  
        self.font = pygame.font.SysFont("simhei", 16)
        self.btn_flag = False # 按钮是否按下的标志
        
    def draw(self):
        '''根据鼠标位置设置颜色  '''
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
        '''检查鼠标点击事件'''
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.btn_flag = True
                print(f"Button '{self.text}' clicked!")
                return self.btn_flag
            
    def set_flag(self, flag):
        '''设置按钮标志位'''
        self.btn_flag = flag
        return self.btn_flag