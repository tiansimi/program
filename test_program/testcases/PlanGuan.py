__author__ = 'HLTQ'
import unittest
from selenium import webdriver
from test_program.common.logger import Logger
from test_program.common.em_planGuanLi import PlanGuanli
import logging
from HTMLTestRunner import HTMLTestRunner


class PlanGuanli_em(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = webdriver.Firefox()
            self.lg = Logger("C:/Users/HLZC/PycharmProjects/TQtest/test_program/logs" + "/Test_LoginEm.log",
                             flevel=logging.INFO)
        except:
            self.lg.logger.error("启动浏览器失败！")

    def test_plan(self):
        self.pl = PlanGuanli(self.driver, url="http://192.168.10.131:8000/EM/DevicePlan/List")
        self.driver.maximize_window()
        self.pl.shaiXuan("00337", "123")



if __name__ == "__main__":
    unittest.main()