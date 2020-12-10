from oneos.util.util import Util
from oneos.pageobject.know_oneos import Know_oneos
import allure
import sys
web=sys.argv[1]
@allure.feature("检查关于oneos页面跳转")
class Test_know:
    def setup_class(self):
        self.know=Know_oneos(web)
    @allure.story('检查关于oneos页面跳转')
    @allure.step('检查跳转后的信息')
    def test_consumer_jump(self):
        know_text=self.know.know_jump()
        assert know_text == "OneOS简介"
        Util(web).save_screenshot(web,"Oneos页面")