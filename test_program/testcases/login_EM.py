__author__ = 'HLTQ'
import unittest
from selenium import webdriver
from test_program.common.logger import Logger
from test_program.common.em_Login import Login
from test_program.common.em_LogOut import LogOut
import logging
import time


class LoginEm(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
            self.lg = Logger("C:/Users/HLZC/PycharmProjects/TQtest/test_program/logs" + "/Test_LoginEm.log",
                             flevel=logging.INFO)

        except:

            self.lg.logger.error("启动浏览器失败！")


    def test_login(self):
        self.lg.info("启动浏览器成功！")
        self.login_em = Login(self.driver, url="http://192.168.10.131:8000/EM")
        self.login_em.go_LoginPage()
        self.login_em.login("00337", "123")
        self.lg.info("wait 2s.")
        time.sleep(2)
        self.driver.refresh()
        self.lg.info("refresh")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__mian__":
    unittest.main()


