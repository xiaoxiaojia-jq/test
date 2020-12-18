import time

from oneos.pageobject.home import Home_page
import allure
import pytest
from oneos.util.util import Util
from selenium.webdriver.common.by import By
import yaml
import sys
web=sys.argv[1]
@allure.feature("首页")

class Testhome_navigation:
    data = Util.load_yaml("../oneos/data/home.data.yaml")
    def setup_class(self):
        self.home_page = Home_page(web)


    @allure.story("导航栏")
    @allure.title("检查导航栏产品功能")
    @allure.severity("normal")
    def test_product_navigation(self):
        with allure.step("检查导航栏产品功能文本"):
            con = self.home_page.check_product()
            assert con == "产品功能"
            Util(web).save_screenshot(web,'检查产品功能导航栏')

    @allure.story("导航栏")
    @allure.title("检查产品功能菜单")
    @allure.severity("normal")
    @pytest.mark.parametrize("name_menu,result_menu", data["test_home_product_menu"])
    def test_product_menu(self,name_menu,result_menu):
        product_text= self.home_page.check_product_menu(name_menu)
        with allure.step("检查"+name_menu+"文本"):
            assert product_text == result_menu
            Util(web).save_screenshot(web,'产品功能菜单')

    @allure.story("导航栏")
    @allure.title("检查产品功能菜单详情")
    @allure.severity("normal")
    @pytest.mark.parametrize("name_details,result_details", data["test_home_product_details"])
    def test_product_details(self,name_details,result_details):
        with allure.step("检查"+name_details+"详情页面"):
            product_text=self.home_page.check_product_details(name_details)
            assert product_text==result_details
            Util(web).save_screenshot(web,name_details+'详情页面')
        Util(web).click(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/a/img')
        time.sleep(1)
    @allure.story("产品功能跳转")
    @allure.title("检查产品功能跳转")
    @allure.severity("normal")
    @pytest.mark.parametrize("name,xpath,result", data["test_home_product_jump"])
    def test_product_jump(self,name,xpath,result):
        with allure.step("检查"+name+"跳转详情页面"):
            product_text=self.home_page.check_product_jump(xpath)
            assert product_text == result
            Util(web).save_screenshot(web,name+"页面跳转")


    @allure.story("导航栏")
    @allure.title("检查导航栏解决方案")
    @allure.severity("normal")
    def test_solve_navigation(self):
        with allure.step("检查导航栏解决方案文本"):
            con = self.home_page.check_solve()
            assert con == "解决方案"
            Util(web).save_screenshot(web,'解决方案文本')

    @allure.story("导航栏")
    @allure.title("检查解决方案菜单")
    @allure.severity("normal")
    @pytest.mark.parametrize("name_menu,result_menu", data["test_home_solve_menu"])
    def test_solve_menu(self,name_menu,result_menu):
        solve_text= self.home_page.check_solve_menu(name_menu)
        with allure.step("检查"+name_menu+"文本"):
            assert solve_text == result_menu
            Util(web).save_screenshot(web,'解决方案'+name_menu+'菜单名')

    @allure.story("导航栏")
    @allure.title("检查解决方案菜单详情")
    @allure.severity("normal")
    @pytest.mark.parametrize("name_details,result_details", data["test_home_solve_details"])
    def test_solve_details(self,name_details,result_details):
        with allure.step("检查"+name_details+"详情页面"):
            solve_text=self.home_page.check_solve_details(name_details)
            assert solve_text==result_details
            Util(web).save_screenshot(web,name_details+"详情页面")
        Util(web).click(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div/a/img')
        time.sleep(1)
    @allure.story('检查解决方案跳转')
    @allure.severity('normal')
    @pytest.mark.parametrize("xpath,result_jump", data["test_home_solve_jump"])
    def test_solve_jump(self,xpath,result_jump):
            solve_text=self.home_page.check_solve_jump(xpath)
            assert solve_text==result_jump
            Util(web).save_screenshot(web,"解决方案详情页面")
            Util(web).click(By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div/a/img')
            time.sleep(2)

    @allure.story('检查大标题')
    @allure.severity('normal')
    @pytest.mark.parametrize("xpath,result_big_title", data["test_home_big_title"])
    def test_big_title(self,xpath,result_big_title):
            big_title_text = self.home_page.check_big_title(xpath)
            assert big_title_text == result_big_title
            Util(web).save_screenshot(web,"大标题检查")


    @allure.story('检查底部信息')
    @allure.severity('normal')
    @pytest.mark.parametrize("botton_name,xpath,result_bottom", data["test_home_bottom_information"])
    def test_bottom_information(self,botton_name,xpath,result_bottom):
        with allure.step("检查"+botton_name+"固定信息"):
            bottom_information_text=self.home_page.check_bottom_information(xpath)
            assert result_bottom in bottom_information_text
            Util(web).save_screenshot(web,"底部信息"+botton_name+"检查")
