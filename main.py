import os
import sys
import unittest
import socket

from time import sleep
from appium import webdriver

class AppiumTest(unittest.TestCase):
    def setUp(self):
        options = {
            'logLevel': 'info',
            'platformName': 'iOS',
            'deviceName': 'iPhone 14 Pro',
            'platformVersion': '16.0',
            'automationName': 'XCUITest',
            'bundleId': 'devnokiyo.AppiumDemo.test-app', # ここを編集
        }

        protocol = 'http'
        host = '0.0.0.0'
        ipaddress = '0.0.0.0'
        port = '4723'
        path = '/wd/hub'
        self.driver = webdriver.Remote(f'{protocol}://{ipaddress}:{port}{path}', options)


    def tearDown(self):
        self.driver.quit()

    def test_textfield(self):
        element = self.driver.find_element("accessibility id","textField")

        # 値を取得
        value = element.get_attribute('value')
        self.assertEqual(value, None)

        # テキストを入力
        word = "Hello, World!"
        element.send_keys(word)

        # 値を取得
        value = element.get_attribute('value')
        self.assertEqual(value, word)

if __name__ == '__main__':
    # テストを実行
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

