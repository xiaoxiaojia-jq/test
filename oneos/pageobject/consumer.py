import time
from oneos.util.util import Util
from selenium.webdriver.common.by import By

class Consumer:
    def __init__(self,web):
        self.consumer = Util(web)
    def consumer_jump(self,web):
        windown1 = self.consumer.dr.current_window_handle
        self.consumer.click(By.LINK_TEXT, '社区论坛')
        self.consumer.change_windown(windown1)
        consumer_text = self.consumer.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/ul/li[1]')
        self.consumer.save_screenshot(web,"社区论坛页面")
        Util.dr.close()
        Util.dr.switch_to_window(windown1)
        return consumer_text