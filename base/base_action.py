import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base_action:
    # 获取对象
    def __init__(self, driver):
        self.driver = driver
    # 点击
    def click(self, loc):
        self.find_element(loc).click()
    #输入txt
    def input_txt(self,loc,txt):
        self.find_element(loc).send_keys(txt)
    #获取txt
    def get_txt(self,loc):
        return self.find_element(loc).text

    def quit(self):
        self.driver.quit()
    def assertin(self, expected, actual, screen = "AssertionError"):
        try:
            assert expected in actual
        except AssertionError:
            # 设置时间
            now_time = time.strftime('%Y-%m-%d_%H:%M:%S')
            # 截图
            self.screenshot(screen + now_time)
            # 上传图片到报告
            allure.attach(open("./screen/" + screen + now_time + ".png", "rb").read(), "失败截图", allure.attachment_type.PNG)
            # print("预期结果为：%s  实际结果为%s" % (expected, actual))
            raise AssertionError


    # 处理参数
    def find_element(self, loc):
        if type(loc) == str:
            by = By.XPATH
            value = self.make_xpath_with_feature(loc)
        else:
            by = loc[0]
            value = loc[1]

        return WebDriverWait(self.driver, 5, 1).until(lambda x:x.find_element(by, value))

    def make_xpath_with_feature(self, loc):

        feature_start = "//*["
        feature_end = "]"
        if isinstance(loc, str):
            if loc.startswith("//"):
                return loc
            elif loc.startswith("@"):
                feature = loc
                return feature_start + feature + feature_end
            else:
                feature = "@" + loc
                return feature_start + feature + feature_end
    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./screen/" + file_name + ".png")