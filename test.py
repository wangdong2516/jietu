from selenium import webdriver
import numpy as np
import time
from PIL import Image


def get_page_image():
    option = webdriver.ChromeOptions()
    # 无头模式
    option.add_argument('headless')
    # 沙盒模式运行
    option.add_argument('no-sandbox')
    # 大量渲染时候写入/tmp而非/dev/shm
    option.add_argument('disable-dev-shm-usage')
    # 指定驱动路径
    browser = webdriver.Chrome('/usr/bin/chromedriver',options=option)
    # 获取一个全屏窗口
    browser.fullscreen_window()
    # 访问百度
    browser.get('https://ljnewlifestyle.com')
    # 窗口高度
    window_height = browser.get_window_size()['height']
    # 页面高度
    page_height = browser.execute_script('return document.documentElement.scrollHeight')
    page_weight = browser.execute_script('return document.documentElement.scrollWidth')
    # 打印标题
    print(browser.title)
    print(page_weight, page_height)
    # if page_height > window_height:
    #     n = page_height // window_height  # 需要滚动的次数
    #     base_mat = np.atleast_2d(Image.open('test.png'))  # 打开截图并转为二维矩阵
    #
    #     for i in range(n):
    #         browser.execute_script(f'document.documentElement.scrollTop={window_height*(i+1)};')
    #         time.sleep(.5)
    #         browser.save_screenshot(f'qq_{i}.png')  # 保存截图
    #         mat = np.atleast_2d(Image.open(f'qq_{i}.png'))  # 打开截图并转为二维矩阵
    #         base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
    #     Image.fromarray(base_mat).save('hao123.png')
    browser.set_window_size(page_weight, page_height)
    browser.save_screenshot('test.png')
    # 关闭浏览器
    browser.quit()