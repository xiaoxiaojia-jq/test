import time
from oneos.util.util import Util
from selenium.webdriver.common.by import By

class Know_oneos:
    def __init__(self,web):
        self.know = Util(web)
    def know_jump(self):
        self.know.click(By.LINK_TEXT, '关于OneOS')
        try:
            know_text = self.know.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[3]/div[1]/div[2]')
            return know_text
        except:
            return "参数未找到"