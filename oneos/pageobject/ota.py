
from oneos.util.util import Util
from selenium.webdriver.common.by import By

class Ota_page:
    def __init__(self,web):
        self.ota = Util(web)
    def ota_introduction(self):
        windows_1 = self.ota.dr.current_window_handle
        try:
            self.ota.move_to(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/div[1]/div[4]/span[2]')
            self.ota.click(By.LINK_TEXT, 'OTA云平台')
            self.ota.change_windown(windows_1)
            ota_text=self.ota.get_text(By.XPATH,'//*[@id="__layout"]/div/div[2]/div[2]/div[2]')
            Util.dr.close()
            Util.dr.switch_to_window(windows_1)
            return ota_text
        except:
            return '参数未找到'