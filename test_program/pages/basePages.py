__author__ = 'HLTQ'
from test_program.common.logger import Logger


class Basepage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except:

            self.path = "C:/Users/HLZC/PycharmProjects/TQtest/test_program/logs"
            self.lg = Logger(self.path + "/base_page.log")
            self.lg.error("找不到元素！%s"%str(loc))


    def send_keys(self, loc, text):
        try:
            self.find_element(*loc).send_keys(text)
        except:
            self.lg.error("输入失败：%s" % text)

    def click(self, loc):  # 点击
        try:
            self.find_element(*loc).click()
        except:
            self.lg.error("点击失败：%loc" % str(loc))

    def clear_input(self, loc):
        self.find_element(*loc).clear()
