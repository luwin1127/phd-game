import pygame  
import sys 
import json
import Button

"""----------------------1.1 设置初始参数----------------------"""
version = '0.1.0'               # 游戏版本
author = "Lingwei Li"           # 游戏作者
pygame.init()                   # 初始化
window_width = 800              # 窗口宽度
window_height = 600             # 窗口高度
margin = 10                     # 间隔
yr, mh = 1, 1                   # 年份、月份
click_num = 0
hope = 100                     # 毕业希望
window = pygame.display.set_mode((window_width, window_height))     # 初始化显示窗口
pygame.display.set_caption("博士研磨记")                             # 设置窗口标题  
"""----------------------1.2 设置颜色参数----------------------"""
bg_color = (111, 202, 239)      # 背景颜色
box_color = (255, 244, 225)     # 文字框颜色
shadow_color = (91, 145, 165)   # 阴影颜色
frame_color = (98, 83, 74)      # 边框颜色
btn_color = (245, 222, 179)     # 按钮颜色
btn_frm_color = (220, 190, 74)  # 按钮边框颜色
btn_frm_change_color = (164, 136, 83) # 按钮边框选中颜色
text_color = (0, 0, 0)          # 文字颜色
"""----------------------1.3 设置画布参数----------------------"""
start_surface = pygame.Surface(window.get_size())
start_surface = start_surface.convert()     # 使用convert可以转换格式，提高blit的速度
start_surface.fill(bg_color)
"""----------------------1.4 设置边框参数----------------------"""
factor = 1.3                        # 阴影扩散因子
divide = 20                         # 高度划分格数
base_width = window_width-2*margin  # 基准宽度
base_height = window_height/divide  # 基准高度
"""----------------------1.5 设置标志参数----------------------"""
login_flag = True                                               # 登录窗口的标志
isgame_flag = True                                              # 控制游戏进行的标志
exit_flag = True                                                # 弹出游戏结束窗口的标志
game_flag = "start"
"""----------------------1.6 设置字体参数----------------------"""
font_version = pygame.font.SysFont("segoeuisemibold", 11)       # 添加字体
font = pygame.font.SysFont("simhei", 18)                        # 黑体
font_small = pygame.font.SysFont("simhei", 16)
"""----------------------1.7 导入游戏数据----------------------"""
with open('./data/message.json', 'r', encoding='utf-8') as f:  
    message = json.load(f)

with open('./data/button.json', 'r', encoding='utf-8') as f:  
    button = json.load(f)

with open('./data/items.json', 'r', encoding='utf-8') as f:  
    items = json.load(f)

with open('./data/status.json', 'r', encoding='utf-8') as f:
    status = json.load(f)

with open('./data/flags.json', 'r',  encoding='utf-8') as f:
    flags = json.load(f)
bg_music = pygame.mixer.Sound('./music/BGM074.ogg')             # 导入音乐
"""----------------------2 游戏开始----------------------"""
info_str = message['welcome']
btn4_str = button['reject']
btn3_str = button['accept']
bg_music.play()                                                 # 播放音乐
while isgame_flag:  
  
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
    hope_str = "毕业希望 {}/100".format(hope)                            # 创建文字对象
    hope_text = font.render(hope_str, True, text_color, box_color)      # 设置文字
    window.blit(hope_text, (20*margin, 1.5*margin))                     # 显示在窗口中
    
    time_str = "第 {} 年 {} 月".format(yr, mh)                           # 创建文字对象
    time_text = font.render(time_str, True, text_color, box_color)      # 设置文字
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

    # 矩形四个顶点坐标
    top_left = (rect_box.x, rect_box.y)                             # 左上角
    top_right = (rect_box.x+rect_box.w, rect_box.y)                 # 右上角
    bottom_left = (rect_box.x, rect_box.y+rect_box.h)               # 左下角
    bottom_right = (rect_box.x+rect_box.w, rect_box.y+rect_box.h)   # 右下角

    # 显示文字
    # info_str = message['welcome']
    info_text = font.render(info_str, True, text_color, box_color)
    info_text_width, info_text_height = info_text.get_size()
    window.blit(info_text, (rect_box.x+margin,rect_box.y+margin))

    # 按钮区（从下往上建立）
    # 第四个按钮
    if game_flag == "start" or game_flag == "end1":
        reject_btn = Button.Button(window, btn4_str, bottom_left[0]+margin, bottom_left[1]-base_height*2, base_width-2*margin, base_height*1.5)
        reject_btn.draw()

    # 第三个按钮
    if game_flag == "start":
        accept_btn = Button.Button(window, btn3_str, bottom_left[0]+margin, bottom_left[1]-base_height*3.5-0.5*margin, base_width-2*margin, base_height*1.5)  
        accept_btn.draw()

    # 第1年1月不显示这俩按钮
    if game_flag != "start" and game_flag != "end1":
        # 第二个按钮
        button2 = Button.Button(window, "选择2", bottom_left[0]+margin, bottom_left[1]-base_height*5-1*margin, base_width-2*margin, base_height*1.5)
        button2.draw()

        # 第一个按钮
        button1 = Button.Button(window, "选择1", bottom_left[0]+margin, bottom_left[1]-base_height*6.5-1.5*margin, base_width-2*margin, base_height*1.5)
        button1.draw()

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
    item_text = font.render("物品：", True, text_color, box_color)      # 设置文字
    item_text_width, item_text_height = item_text.get_size()          # 得到文字位置
    window.blit(item_text, (rect_box.x+margin,rect_box.y+margin))      # 显示在窗口中


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
    status_text = font.render("状态：", True, text_color, box_color)      # 设置文字
    status_text_width, status_text_height = status_text.get_size()        # 得到文字位置
    window.blit(status_text, (margin+rect_box.x, margin+rect_box.y))      # 显示在窗口中

    # 状态1
    status_text1_str = status['first_year']['content']
    status_text1 = font_small.render(status_text1_str, True, text_color, box_color)
    status_text1_width, status_text1_height = status_text.get_size()
    window.blit(status_text1, (margin+rect_box.x, 1.5*margin+rect_box.y+status_text_height))

    # 最下方的版权和版本号
    # -------------------------------------------------------------------------------------------------------- #
    #  Copyright © 2024 {author}. All rights reserved.  |  Ver {version}
    # -------------------------------------------------------------------------------------------------------- #
    copyright_str = "Copyright © 2024 {}. All rights reserved.  |  ".format(author)                 # 版权信息
    version_str = "Ver {}".format(version)                                                          # 版本信息
    bottom_text = font_version.render(copyright_str+version_str, True, (255,255,255), bg_color)     # 版权和版本合在一起
    bottom_text_width, bottom_text_height = bottom_text.get_size()
    window.blit(bottom_text, ((window_width-bottom_text_width)/2, window_height-1.5*margin))        # 显示出来

    # -------------------------------------------------------------------------------------------------------- #
    # 处理事件队列  
    # -------------------------------------------------------------------------------------------------------- #
    
    # accept_btn = Button.Button(window, btn3_str, bottom_left[0]+margin, bottom_left[1]-base_height*3.5-0.5*margin, base_width-2*margin, base_height*1.5)  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            isgame_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(game_flag)
            accept_btn_flag = accept_btn.handle_event(event)
            reject_btn_flag = reject_btn.handle_event(event)
                    
            if game_flag == "start":
                if reject_btn_flag:             # 判断是否按下“拒绝按钮”
                    accept_btn.draw_del()
                    game_flag = flags['end1']
                    info_str = message['reject']
                    btn4_str = button['restart']
                    break                       # 跳出循环，不然就一直在event.type == pygame.MOUSEBUTTONDOWN里死循环了
                if accept_btn_flag:             # 判断是否按下“接受”按钮
                    # 点击“接受”按钮日期才会变化（顺序为：宽、高）
                    if bottom_left[0]+margin < event.pos[0] < bottom_left[0]+margin+base_width-2*margin and bottom_left[1]-base_height*3.5-0.5*margin < event.pos[1] < bottom_left[1]-base_height*3.5-0.5*margin+base_height*1.5:
                        mh += 1                 # 月数加1
                        if mh > 12:             # 月数超过12的时候增加年数
                            yr += 1
                            mh = 1
            if game_flag == "end1":
                print(reject_btn_flag)
                if reject_btn_flag:
                    game_flag = flags['start']
                    info_str = message['welcome']
                    btn4_str = button['reject']
                    btn3_str = button['accept']
                    break
            
    
    # -------------------------------------------------------------------------------------------------------- #
    # 游戏逻辑部分
    # -------------------------------------------------------------------------------------------------------- #

  
    # 更新屏幕显示  
    pygame.display.flip()  
  
    # 控制帧率  
    pygame.time.Clock().tick(24)  
  
# 退出游戏  
pygame.quit()  
sys.exit()