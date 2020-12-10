
from oneos.pageobject.consumer import Consumer
import allure
import sys
print(sys.argv)
web=sys.argv[1]

@allure.feature("检查社区论坛跳转")
class Test_consumer:
    def setup_class(self):
        self.consumer=Consumer(web)

    @allure.story('检查社区论坛页面跳转')
    @allure.step('检查跳转后的信息')
    def test_consumer_jump(self):
        consumer_text=self.consumer.consumer_jump(web)
        assert consumer_text=="热门"
