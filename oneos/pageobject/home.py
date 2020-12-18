import time

from oneos.util.util import Util
from selenium.webdriver.common.by import By

class Home_page:
    def __init__(self,web):
        self.home = Util(web)
    def check_product(self):
        # 检查产品功能
        try:
            product_text = self.home.get_text(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[1]/span[2]')
            return product_text
        except:
            return "参数未找到"
    #检查菜单名
    def check_product_menu(self,product_name):
        try:
            self.home.move_to(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[1]/span[2]')
            product_text = self.home.get_text(By.LINK_TEXT, product_name)
            return product_text
        except:
            return "参数未找到"

    #检查菜单详情
    def check_product_details(self,product_name):
        self.home.move_to(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[1]/span[2]')
        self.home.click(By.LINK_TEXT,product_name)
        try:
            product_text = self.home.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[3]/div[1]/div[2]')
            return product_text
        except:
            return "参数未找到"

    #检查菜单页面跳转
    def check_product_jump(self,XPATH):
        time.sleep(2)
        self.home.move_to(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[3]/div[2]/div[1]/img')
        window_1 = self.home.dr.current_window_handle
        try:
            self.home.click(By.XPATH,XPATH)
            self.home.click(By.LINK_TEXT,"立即体验")
            self.home.change_windown(window_1)
            product_text = self.home.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[3]/div[1]/div[2]')
            Util.dr.close()
            Util.dr.switch_to.window(window_1)
            return product_text
        except:
            Util.dr.close()
            Util.dr.switch_to.window(window_1)
            return "参数未找到"
    #检查解决方案
    def check_solve(self):
        # 检查产品功能
        self.home.move_to(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[2]/span[2]')
        try:
            solve_text = self.home.get_text(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[2]/span[2]')
            return solve_text
        except:
            return "参数未找到"
    #检查菜单名
    def check_solve_menu(self,solve_name):
        self.home.move_to(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[2]/span[2]')
        try:
            product_text = self.home.get_text(By.LINK_TEXT, solve_name)
            return product_text
        except:
            return '参数未找到'

    #检查菜单详情
    def check_solve_details(self,solve_name):
        self.home.move_to(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[2]/span[2]')
        try:
            self.home.click(By.LINK_TEXT,solve_name)
            solve_text = self.home.get_text(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[3]/div[1]/div[2]')
            return solve_text
        except:
            return '参数未找到'

    #检查解决方案跳转
    def check_solve_jump(self,xpath):
        time.sleep(1)
        try:
            self.home.dr.find_element_by_xpath(xpath).click()
            self.home.dr.find_element_by_link_text('查看更多').click()
            solve_text=self.home.get_text(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[3]/div[1]/div[2]')
            return solve_text
        except:
            return '参数未找到'
    #大标题检查
    def check_big_title(self,big_title):
        try:
            self.home.move_to(By.XPATH,big_title)
            time.sleep(0.5)
            big_title_text=self.home.get_text(By.XPATH,big_title)
            return big_title_text
        except:
            return '参数未找到'

    #底部固定信息检查
    def check_bottom_information(self,bottom_information):
        try:
            self.home.move_to(By.XPATH,bottom_information)
            bottom_information_text=self.home.get_text(By.XPATH,bottom_information)
            return bottom_information_text
        except:
            return '参数未找到'

