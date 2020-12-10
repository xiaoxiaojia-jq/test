from oneos.util.util import Util
from oneos.pageobject.ota import Ota_page
import allure
import sys
web=sys.argv[1]
@allure.feature('ota介绍页检查')
class Test_ota:
    def setup_class(self):
        self.ota = Ota_page(web)
    def teardown_class(self):
        Util(web).close_driver()
    @allure.story('ota页面检查')
    def test_ota(self):
        with allure.step('检查OTA介绍页面简介内容'):
            ota_text,windows_1=self.ota.ota_introduction()
            assert ota_text=='OTA云平台是OneOS提供的升级管理平台，' \
                             '满足客户对项目管理、版本管理、多策略配置、数据统计分析、差分算法等升级能力的管理。' \
                             '设备端通过对SDK的集成，获得网络连接、最新版本检测、升级包下载、安全校验、差分还原、' \
                             '写入升级的能力。在完善的安全体系和灾备体系下实现对整个OTA业务的运营和监管。'
            Util(web).save_screenshot(web,'ota介绍页')
            Util.dr.close()
            Util(web).dr.switch_to_window(windows_1)