import pytest
import os
import sys

with open("xxx1.txt", "w")as f:
    f.write(str(sys.argv))
web=sys.argv[1]
# 用pytest把结果生成到result中
pytest.main(['-v', 'testcase', '--alluredir', './result_'+web, "--clean-alluredir"])
# 趋势图数据
os.system('xcopy report_'+web+'\history result_'+web+'\history /e /Y /I')
# allure生成测试报告
os.system('allure generate ./result_'+web+' -o ./report_'+web+' --clean')
# 环境变量
# os.system('copy environment.properties report\environment.properties')
# if __name__ == '__main__':
#     os.system('python runCase.py Chrome')
