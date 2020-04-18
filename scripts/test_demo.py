import os, sys

import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver_calculator
from base.base_data import get_yml_data_with_filename_key
from time import sleep
import pytest
from page.demo_page import Demo_page

def data_with_key(key):
    return get_yml_data_with_filename_key('data', key)


class Test_demo:
    def setup_class(self):
        self.driver = init_driver_calculator()
        self.demo_page = Demo_page(self.driver)

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    @allure.step(title="demo的测试脚本")
    # 设置执行顺序=1
    @pytest.mark.run(order=1)
    # 设置预言失败为False
    @pytest.mark.xfail(False, reason="")
    # 参数化
    @pytest.mark.parametrize("args", data_with_key('test_demo'))
    def test_demo(self,args):
        num1 = args["num1"]
        ysf = args["ysf"]
        num2 = args["num2"]
        zhi = args["zhi"]
        allure.attach("测试运算是否正确", "测试")
        self.demo_page.yunsuan(num1, ysf, num2)
        self.demo_page.assertin_jieguo(zhi)

if __name__ == '__main__':
    pytest.main("-s test_demo.py")