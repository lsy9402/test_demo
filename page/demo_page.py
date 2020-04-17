import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import Base_action


class Demo_page(Base_action):
    # 运算按钮
    def yunsuanfu(self, ysf):
        if ysf == '+':
            return 'content-desc="加"'
        elif ysf == '-':
            return (By.ID, "com.android.calculator2:id/op_sub")
        elif ysf == '*':
            return '@content-desc="×"'
            # return (By.ID, "com.android.calculator2:id/op_mul")
        elif ysf == '/':
            return (By.ID, "com.android.calculator2:id/op_div")
    # 数字按钮（+input）
    def num(self, num):
        str(num)
        return (By.ID, "com.android.calculator2:id/digit_%s" % num)
    # 按钮=
    eq = (By.ID, "com.android.calculator2:id/eq")

    # 计算结果定位
    jieguotxt = (By.ID, "com.android.calculator2:id/result")
    def assertin_jieguo(self, expected):
        expected_str = str(expected)
        return self.assertin(expected_str, self.get_txt(self.jieguotxt))


    # 搜索框输入文本
    def yunsuan(self, num1, yunsuanfu, num2):
        self.click(self.num(num1))
        self.click(self.yunsuanfu(yunsuanfu))
        self.click(self.num(num2))
        self.click(self.eq)

