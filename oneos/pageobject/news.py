import time
from oneos.util.util import Util
from selenium.webdriver.common.by import By

class News:
    def __init__(self,web):
        self.News_page = Util(web)
    def news_jump(self):
        self.News_page.click(By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div[1]/div[1]/div[2]/a[3]')
        know_text = self.News_page.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[1]/div[1]/a/span')
        return know_text
    def news_detials(self):
        news_detials=self.News_page.get_text(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/a/div/div[1]')
        self.News_page.click(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/div[2]/div[1]/a')
        new=self.News_page.get_text(By.XPATH,'//*[@id="__layout"]/div/div[2]/div/div[1]/div[2]/div[1]')
        return news_detials,new