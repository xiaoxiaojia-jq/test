import datetime
import os
import time
from time import sleep
import pytest
import allure
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

class Util:
    dr = None
    @classmethod
    def __init__(cls,web):
        if web=="Chrome" :
            if cls.dr == None:
                cls.dr = webdriver.Chrome()
                cls.dr.maximize_window()
                cls.dr.get("https://test.os.cmiotcd.com:28443/")
                cls.dr.implicitly_wait(12)
        if web =="Firefox":
            if cls.dr == None:
                cls.dr = webdriver.Firefox()
                cls.dr.maximize_window()
                cls.dr.get("https://test.os.cmiotcd.com:28443/")
                cls.dr.implicitly_wait(12)
        if web =="Ie":
            if cls.dr == None:
                cls.dr = webdriver.Ie()
                cls.dr.maximize_window()
                cls.dr.get("https://test.os.cmiotcd.com:28443/")
                cls.dr.implicitly_wait(12)


    def close_driver(self):
        """
        关闭 driver
        """
        sleep(2)
        self.dr.quit()

    def find(self, by, locator=""):
        """
        查找元素

        :param by: 定位方式
        :param locator: 定位符
        :return: 元素对象
        """
        if isinstance(by, tuple):
            return self.dr.find_element(*by)
        else:
            return self.dr.find_element(by, locator)

    def click(self, by, locator=""):
        """
        点击元素

        :param by: 定位方式
        :param locator: 定位符
        """
        self.find(by, locator).click()

    def input(self, kw: str, by, locator=""):
        """
        输入字符串到元素

        :param kw: 输入字符
        :param by: 定位方式
        :param locator: 定位符
        """
        element = self.find(by, locator)
        element.clear()
        element.send_keys(kw)

    def move_to(self, by, locator=""):
        """
        模拟鼠标悬停在某个位置

        :param by: 定位方式
        :param locator: 定位符
        """
        element = self.find(by, locator)
        chain = ActionChains(self.dr)
        chain.move_to_element(element).perform()

    def get_title(self):
        """
        获取当前网页的标题

        :return: 网页标题
        """
        return self.dr.title
    def change_windown(self,window_1):
        # 获得打开的所有的窗口句柄
        windows = self.dr.window_handles
        # 切换到最新的窗口
        for current_window in windows:
            if current_window != window_1:
                self.dr.switch_to.window(current_window)

    def get_url(self):
        """
        获取当前网页的地址
        :return: URL
        """
        return self.dr.current_url

    def get_text(self, by, locator=""):
        """
        获取元素的文本

        :return: 元素文本
        """
        return self.find(by, locator).text

    def get_location(self, by, locator=""):
        """
        获取元素的位置

        :param by: 定位方式
        :param locator: 定位符
        """
        return self.find(by, locator).location


    def is_displayed(self, by, locator=""):
        """
        查看元素是否显现

        :param by: 定位方式
        :param locator: 定位符
        :return 元素是否显现（Ture/False）
        """
        return self.find(by, locator).is_displayed()

    def save_screenshot(self, web,img_doc):
        """
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        """
        file_name = './result_'+web+'/png/' + img_doc + time.strftime("%Y-%m-%d-%H-%M-%S") + ".png"
        self.dr.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)


    @classmethod
    def load_yaml(cls, path):
        """
        加载yaml文件
        """
        with open(path,'r',encoding='UTF-8') as f:  # 如果不写编码方式，会出现 UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position
            return yaml.safe_load(f)

