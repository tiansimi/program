__author__ = 'HLTQ'
from selenium.webdriver.common.by import By
from test_program.pages.basePages import Basepage
import time

class Login(Basepage):
    # 用户名输入框的id
    username_Id = (By.ID, "UserName")
    # 密码  输入框的ID
    psw_Id = (By.ID, "Password")
    # 登录按钮的Xpath
    login_button = (By.XPATH, ".//div[@class = 'form-actions']/button")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_LoginPage(self):
        self.driver.get(self.url)

    def login(self, username, psw):
        self.clear_input(self.username_Id)
        self.send_keys(self.username_Id, username)
        self.clear_input(self.psw_Id)
        self.send_keys(self.psw_Id, psw)
        self.click(self.login_button)
        time.sleep(3)
        assert "首页" in self.driver.title, "打开首页失败！"







