__author__ = 'HLTQ'
from selenium.webdriver.common.by import By
from test_program.pages.basePages import Basepage


class LogOut(Basepage):
    # 登出超文本链接
    out_link_text = (By.LINK_TEXT, "登出")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def logOut(self):  # 点击登出
        self.click(self.out_link_text)



