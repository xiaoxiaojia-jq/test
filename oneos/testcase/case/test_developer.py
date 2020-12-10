import time

from oneos.pageobject.developer import Developer
import allure
import pytest
from oneos.util.util import Util
from selenium.webdriver.common.by import By
import sys
web=sys.argv[1]
@allure.feature("开发者中心")
class Test_developer:
    ata = Util.load_yaml("../oneos/data/home.data.yaml")

    def setup_class(self):
        self.developer_page = Developer(web)

    # def teardown_class(self):
    #     Util().close_driver()
    @allure.title("检查oneos下载页面")
    @allure.story('检查oneos下载页面111')
    def test_down(self):
        with allure.step("检查下载按钮是否存在"):
            developer_down_text=self.developer_page.developer_down(web)
            assert developer_down_text=="点击下载"

    @allure.title("检查开发文档页面")
    @allure.story('检查开发文档页面')
    def test_file(self):
        with allure.step("检查开发文档页面信息"):
            file_text = self.developer_page.developer_file(web)
            assert file_text == "OneOS 是中国移动针对物联网领域推出的轻量级操作系统，" \
                        "具有可裁剪、跨平台、低功耗、高安全等特点，支持ARM Cortex-M、MIPS、RISC-V等主流芯片架构，" \
                        "兼容POSIX、CMSIS等标准接口，支持MicroPython语言开发，提供图形化开发工具，能够有效提升开发效率并降低开发成本，" \
                        "帮助用户开发稳定可靠、安全易用的物联网应用。"
