from appium import webdriver
import time
from Appium.Demo.Utility import Desired_Capabilities
from Appium.Demo.Utility import Appium_Server
from Appium.Demo.Utility import Data_Sheet
from Appium.Demo.Utility import Locators
import pytest


@pytest.fixture()
@pytest.mark.run(order=1)
def test_visitor_server_setup():
    global visitor_driver
    desired_capabilities_1 = Desired_Capabilities.DesiredCapabilities.desired_cap_1
    visitor_server = Appium_Server.Server.Server1
    visitor_driver = webdriver.Remote(visitor_server, desired_capabilities_1)


@pytest.fixture()
@pytest.mark.run(order=3)
def test_app_server_setup():
    global app_driver
    desired_capabilities_2 = Desired_Capabilities.DesiredCapabilities.desired_cap
    app_server = Appium_Server.Server.Server2
    app_driver = webdriver.Remote(app_server, desired_capabilities_2)


@pytest.mark.run(order=2)
def test_visitor(test_visitor_server_setup):
    visitor_driver.get(Data_Sheet.input.Visitor_URL)
    visitor_driver.switch_to.frame(visitor_driver.find_element_by_xpath(Locators.Locators.Visitor_Chat_Frame))
    visitor_driver.find_element_by_id(Locators.Locators.Visitor_Chat_Icon).click()
    visitor_driver.find_element_by_id(Locators.Locators.Visitor_Text_Area).send_keys(Data_Sheet.input.Visitor_input)
    visitor_driver.press_keycode(Data_Sheet.input.Enter_Key_Code)


@pytest.mark.run(order=4)
def test_app(test_app_server_setup):
    print(2)
    time.sleep(10)
    app_driver.find_element_by_id(Locators.Locators.Main_app_button).click()
    time.sleep(10)







# Main Code
# desired_cap_1 = {
#     "avd": "Nexus_5X_API_27",
#     "deviceName": "emulator-5554",
#     "platformName": "Android",
#     "browserName": "Chrome",
#     'chromeOptions': {
#         'androidPackage': 'com.android.chrome',
#     }
# }
# driver_1 = webdriver.Remote("http://0.0.0.0:4725/wd/hub", desired_cap_1)
# driver_1.get('https://happyfoxchat.net/chat/cddbd680-43bc-11e9-8e90-4351c25790c9')
# print("start")
# time.sleep(10)
# driver_1.switch_to.frame(driver_1.find_element_by_xpath("//*[@id=\"hfc-frame\"]"))
# # time.sleep(10)
# driver_1.find_element_by_id("hfc-badge").click()
# print("done")
# driver_1.find_element_by_id("reply-textarea").send_keys("Hi")
# print("done1")
# time.sleep(10)
# print("done1")
# # driver_1.press_keycode(66)
# driver_1.find_element_by_xpath(".//*[@name='send-icon']").click()
#
# print("done2")
#
# desired_cap = {
#     "avd": "Pixel_3_XL_API_28",
#     "deviceName": "emulator-5554",
#     "platformName": "Android",
#     "app": "/Users/tenmiles/Downloads/AirMirror Remote control devices_v1.0.3.3_apkpure.com.apk",
#     "appPackage": "com.sand.airmirror",
#     "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
# }
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# time.sleep(10)
# driver.find_element_by_id("com.sand.airmirror:id/tvRegister").click()
# time.sleep(10)
# driver.quit()





#  Unit Test ty
#  Class AppiumTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         dcap = Desired_Capabilities.DesiredCapabilities.desired_cap_1
#         serv = Appium_Server.Server.Server1
#         cls.driver_1 = webdriver.Remote(serv, dcap)
#
#     def test_login(self):
#         driver_1 = self.driver_1
#         driver_1.get('https://happyfoxchat.net/chat/cddbd680-43bc-11e9-8e90-4351c25790c9')
#         time.sleep(10)
#
# class AppiumTest_1(unittest.TestCase):
#
#
#     @classmethod
#     def setUpClass(cls):
#         dcap_2 = Desired_Capabilities.DesiredCapabilities.desired_cap
#         serv_1 = Appium_Server.Server.Server2
#         cls.driver_2 = webdriver.Remote(serv_1, dcap_2)
#
#     def test_launchapp(self):
#         driver_2 = self.driver_2
#         time.sleep(10)
#         driver_2.find_element_by_id("com.sand.airmirror:id/tvRegister").click()
#         time.sleep(10)
