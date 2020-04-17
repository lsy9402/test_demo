import os, sys

# import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver_calculator
from base.base_data import get_data_yml
from time import sleep
import pytest
from page.demo_page import Demo_page

class Test_demo:
    def setup_class(self):
        self.driver = init_driver_calculator()
        self.demo_page = Demo_page(self.driver)

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    # @allure.step(title="demo的测试脚本")
    # 设置执行顺序=1
    @pytest.mark.run(order=1)
    # 设置预言失败为False
    @pytest.mark.xfail(False, reason="")
    # 参数化
    @pytest.mark.parametrize(["num1", "ysf", "num2", "zhi"], get_data_yml())
    def test_demo(self,num1, ysf, num2, zhi):
        # 运算8*6
        # allure.attach("测试运算是否正确", "测试")
        self.demo_page.yunsuan(num1, ysf, num2)
        self.demo_page.assertin_jieguo(zhi)

if __name__ == '__main__':
    pytest.main("-s test_demo.py")