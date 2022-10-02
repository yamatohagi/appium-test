import os
import sys
import unittest
import socket

from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AppiumTest(unittest.TestCase):
    def setUp(self):
        options = {
            "logLevel": "info",
            "platformName": "iOS",
            "deviceName": "iPhone - yamato",
            "platformVersion": "16.0.2",
            "automationName": "XCUITest",
            "startIWDP": "true",
            "showXcodeLog": "true",
            "bundleId": "com.yudo.SaitouSan",  # ここを編集
            "udid": "00008101-001254320191001E",
            "xcodeOrgId": "CUYU636622",
            "xcodeSigningId": "iPhone Developer",
            "newCommandTimeout": 3600,
        }

        protocol = "http"
        host = "0.0.0.0"
        ipaddress = "0.0.0.0"
        port = "4723"
        path = "/wd/hub"
        self.driver = webdriver.Remote(
            f"{protocol}://{ipaddress}:{port}{path}", options
        )

    def tearDown(self):
        self.driver.quit()

    def test_textfield(self):
        # トップ画面
        news_el = self.driver.find_element("accessibility id", "bt news off")
        if news_el:
            TouchAction(self.driver).tap(None, 200, 380, 1).perform()  # 斉藤さんと話すボタン
            # 電話とカメラ封印電話を選択するところ
            camera_off_button_el = self.driver.find_element(
                "accessibility id", "bt talk disable camera off"
            )
            TouchAction(self.driver).tap(camera_off_button_el, 1).perform()

            i = 0

            while i < 1000:
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.ID, "相手にコールして通話しよう♪"))
                )

                try:
                    self.driver.find_element("accessibility id", "通話が開始できませんでした")
                    TouchAction(self.driver).tap(None, 250, 460, 1).perform()  # もう一回
                except:
                    try:
                        self.driver.find_element("accessibility id", "男")
                        TouchAction(self.driver).tap(
                            None, 100, 360, 1
                        ).perform()  # 別の人と話す
                        TouchAction(self.driver).tap(
                            None, 250, 460, 1
                        ).perform()  # もう一回
                    except:
                        TouchAction(self.driver).tap(
                            None, 270, 360, 1
                        ).perform()  # 通話する
                        TouchAction(self.driver).tap(
                            None, 250, 460, 1
                        ).perform()  # もう一回

            print(i)
            i += 1

        sleep(100000)


if __name__ == "__main__":
    # テストを実行
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
