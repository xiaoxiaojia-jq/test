from oneos.pageobject.news import News
import allure
from oneos.util.util import Util
import sys
web=sys.argv[1]
@allure.feature('检查新闻页面')
class Test_news:
    def setup_class(self):
        self.new = News(web)
    @allure.story('检查新闻列表页')
    @allure.step('新闻列表')
    def test_new_list(self):
        new_list_text=self.new.news_jump()
        assert new_list_text == '第一届科技国际会展中心'
        Util(web).save_screenshot(web,"新闻列表")
    @allure.story('新闻详情')
    @allure.step('检查新闻详情信息')
    def test_new_detials(self):
        new_detials_text,new = self.new.news_detials()
        assert new_detials_text == new
        Util(web).save_screenshot(web,"新闻详情页面")