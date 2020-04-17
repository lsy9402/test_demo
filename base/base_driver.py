from appium import webdriver
def init_driver(appPackage,appActivity):
    # server启动信息
    desired_caps = dict()
    # # 设备信息模拟器
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "8.0.0"
    desired_caps["deviceName"] = "192.168.56.102:5555"
    # 小米设备信息
    # desired_caps["platformName"] = "Android"
    # desired_caps["platformVersion"] = "8.1.0"
    # desired_caps["deviceName"] = "155ddc3f"

    # 设置app信息
    desired_caps["appPackage"] = str(appPackage)
    desired_caps["appActivity"] = str(appActivity)
    # # 中文
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    # 不重装app
    desired_caps['noReset'] = True
    # 返回对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    # driver.find_element_by_id("com.android.calculator2:id/result").get_property()
    return driver

# 启动计算器
def init_driver_calculator():
    return init_driver("com.android.calculator2", "com.android.calculator2.Calculator")
# 启动百度地图
def init_driver_baidumap():
    return init_driver("com.baidu.BaiduMap", "com.baidu.baidumaps.MapsActivity")

