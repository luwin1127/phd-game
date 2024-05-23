import pygame  
import sys 
import random

version = '0.1.0'               # 游戏版本
author = "Lingwei Li"           # 游戏作者
pygame.init()                   # 初始化
window_width = 800              # 窗口宽度
window_height = 600             # 窗口高度
margin = 10                     # 间隔
yr, mh = 1, 1                   # 年份、月份
score = 100                     # 毕业希望

window = pygame.display.set_mode((window_width, window_height))     # 初始化显示窗口
pygame.display.set_caption("博士研磨记")                             # 设置窗口标题  

# 颜色设置
bg_color = (111, 202, 239)      # 背景颜色
box_color = (255, 244, 225)     # 文字框颜色
shadow_color = (91, 145, 165)   # 阴影颜色
frame_color = (98, 83, 74)      # 边框颜色
btn_color = (245, 222, 179)     # 按钮颜色
btn_frm_color = (220, 190, 74)  # 按钮边框颜色
text_color = (0, 0, 0)          # 文字颜色


# 设置画布
start_surface = pygame.Surface(window.get_size())
start_surface = start_surface.convert()     # 使用convert可以转换格式，提高blit的速度
start_surface.fill(bg_color)

"""----------------------设置边框参数----------------------"""
factor = 1.3                        # 阴影扩散因子
divide = 20                         # 高度划分格数
base_width = window_width-2*margin  # 基准宽度
base_height = window_height/divide  # 基准高度
"""----------------------参数设置完毕----------------------"""

"""----------------------设置其他参数----------------------"""
login_flag = True                                               # 登录窗口的标志
game_flag = True                                                # 控制游戏进行的标志
exit_flag = True                                                # 弹出游戏结束窗口的标志
font_version = pygame.font.SysFont("segoeuisemibold", 11)       # 添加字体
font = pygame.font.SysFont("simhei", 18)                        # 黑体
font_small = pygame.font.SysFont("simhei", 16)
"""----------------------参数设置完毕----------------------"""
while game_flag:  
    # 处理事件队列  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            game_flag = False  
  
    # 清除屏幕  
    window.fill(bg_color)  # 背景颜色
  
    # 第一个框，显示信息
    # -------------------------------------------------------------------------------------------------------- #
    #              毕业希望 xxx / 100                                   第 x 年 x 月                            
    # -------------------------------------------------------------------------------------------------------- #
    rect_box = pygame.Rect(margin, margin, base_width, base_height)                     # 创建矩形对象
    rect_shadow = pygame.Rect(factor*margin, factor*margin, base_width, base_height)    # 创建阴影对象
    
    pygame.draw.rect(window, shadow_color, rect_shadow)                 # 绘制阴影
    pygame.draw.rect(window, box_color, rect_box)                       # 绘制矩形
    pygame.draw.rect(window, frame_color, rect_box, 2)                  # 绘制边框，“2”代表边框宽度

    # 显示文字
    hope_str = "毕业希望 {}/100".format(score)                          # 创建文字对象
    hope_text = font.render(hope_str, True, text_color, box_color)      # 设置文字
    hope_text_width, hope_text_height = hope_text.get_size()             # 得到文字位置
    window.blit(hope_text, (20*margin, 1.5*margin))                     # 显示在窗口中
    
    time_str = "第 {} 年 {} 月".format(yr, mh)                          # 创建文字对象
    time_text = font.render(time_str, True, text_color, box_color)      # 设置文字
    time_text_width, time_text_height = hope_text.get_size()             # 得到文字位置
    window.blit(time_text, (window_width/2+10*margin, 1.5*margin))      # 显示在窗口中

    # 第二个框，显示文字
    # -------------------------------------------------------------------------------------------------------- #
    #  正文内容 
    #  - 选项1
    #  - 选项2
    #  - ...... 
    # -------------------------------------------------------------------------------------------------------- #
    rect_box = pygame.Rect(margin, 2*margin+base_height, base_width, base_height*10)                # 创建矩形对象
    rect_shadow = pygame.Rect(factor*margin, 2.3*margin+base_height, base_width, base_height*10)    # 创建阴影对象

    pygame.draw.rect(window, shadow_color, rect_shadow)             # 绘制阴影
    pygame.draw.rect(window, box_color, rect_box)                   # 绘制矩形
    pygame.draw.rect(window, frame_color, rect_box, 2)              # 绘制边框，“2”代表边框宽度

    # 显示文字
    info_str = "恭喜您收到了我们的博士录取通知书！您愿意来我们学院读博吗？"
    info_text = font.render(info_str, True, text_color, box_color)
    info_text_width, info_text_height = info_text.get_size()
    window.blit(info_text, (rect_box.x+margin,rect_box.y+margin))

    # 第三个框，显示物品
    # -------------------------------------------------------------------------------------------------------- #
    #  物品： 
    #  - 物品1
    #  - 物品2
    #  - ...... 
    # -------------------------------------------------------------------------------------------------------- #
    rect_box = pygame.Rect(margin, 3*margin+base_height*11, base_width, base_height*3.5)                    # 创建矩形对象
    rect_shadow = pygame.Rect(factor*margin, 3.3*margin+base_height*11, base_width, base_height*3.5)        # 创建阴影对象

    pygame.draw.rect(window, shadow_color, rect_shadow)             # 绘制阴影
    pygame.draw.rect(window, box_color, rect_box)                   # 绘制矩形
    pygame.draw.rect(window, frame_color, rect_box, 2)              # 绘制边框，“2”代表边框宽度
    
    # 显示文字
    thing_text = font.render("物品：", True, text_color, box_color)      # 设置文字
    thing_text_width, thing_text_height = thing_text.get_size()          # 得到文字位置
    window.blit(thing_text, (rect_box.x+margin,rect_box.y+margin))      # 显示在窗口中


    # 第四个框，显示状态
    # -------------------------------------------------------------------------------------------------------- #
    #  状态： 
    #  - 状态1
    #  - 状态2
    #  - ...... 
    # -------------------------------------------------------------------------------------------------------- #
    rect_box = pygame.Rect(margin, 4*margin+base_height*14.5, base_width, base_height*3.5)                  # 创建矩形对象
    rect_shadow = pygame.Rect(factor*margin, 4.3*margin+base_height*14.5, base_width, base_height*3.5)      # 创建阴影对象

    pygame.draw.rect(window, shadow_color, rect_shadow)             # 绘制阴影
    pygame.draw.rect(window, box_color, rect_box)                   # 绘制矩形
    pygame.draw.rect(window, frame_color, rect_box, 2)              # 绘制边框，“2”代表边框宽度

    # 显示文字
    state_text = font.render("状态：", True, text_color, box_color)      # 设置文字
    state_text_width, state_text_height = state_text.get_size()          # 得到文字位置
    window.blit(state_text, (margin+rect_box.x, margin+rect_box.y))      # 显示在窗口中

    # 状态1
    state_text1_str = "- 激动人心的第一年"
    state_text1 = font_small.render(state_text1_str, True, text_color, box_color)
    state_text1_width, state_text1_height = state_text.get_size()
    window.blit(state_text1, (margin+rect_box.x, 1.5*margin+rect_box.y+state_text_height))

    # 最下方的版权和版本号
    # -------------------------------------------------------------------------------------------------------- #
    #  Copyright © 2024 {author}. All rights reserved.  |  Ver {version}
    # -------------------------------------------------------------------------------------------------------- #
    copyright_str = "Copyright © 2024 {}. All rights reserved.  |  ".format(author)                 # 版权信息
    version_str = "Ver {}".format(version)                                                          # 版本信息
    bottom_text = font_version.render(copyright_str+version_str, True, (255,255,255), bg_color)     # 版权和版本合在一起
    bottom_text_width, bottom_text_height = bottom_text.get_size()
    window.blit(bottom_text, ((window_width-bottom_text_width)/2, window_height-1.5*margin))        # 显示出来

  
    # 更新屏幕显示  
    pygame.display.flip()  
  
    # 控制帧率  
    pygame.time.Clock().tick(60)  
  
# 退出游戏  
pygame.quit()  
sys.exit()