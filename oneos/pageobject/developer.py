import time
from oneos.util.util import Util
from selenium.webdriver.common.by import By

class Developer:
    def __init__(self,web):
        self.developer = Util(web)
    #下载页面
    def developer_down(self,web):
        self.developer.move_to(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[3]/span[2]')
        windown1=self.developer.dr.current_window_handle
        self.developer.click(By.LINK_TEXT, "OneOS下载")
        self.developer.change_windown(windown1)
        down_text=self.developer.get_text(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div/div[2]')
        Util(web).save_screenshot(web,'下载页面')
        Util.dr.close()
        Util.dr.switch_to_window(windown1)
        return down_text
    def developer_file(self,web):
        self.developer.move_to(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[3]/span[2]')
        windown1 = self.developer.dr.current_window_handle
        self.developer.click(By.LINK_TEXT, "开发文档")
        self.developer.change_windown(windown1)
        file_text = self.developer.get_text(By.XPATH, '//*[@id="book-search-results"]/div[1]/div/p[1]')
        Util(web).save_screenshot(web,'开发文档页面')
        Util.dr.close()
        Util.dr.switch_to_window(windown1)
        return file_text


