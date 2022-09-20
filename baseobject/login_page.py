from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage)
    url = "https://weapp.yunteams.cn/"
    #封装页面元素
    account_loc = (By.XPATH, '//input[@type="text"]')
    password_loc = (By.XPATH, '//input[@type="password"]')
    submit_loc = (By.XPATH,'//button[@weid="_mtgi04_6p6nql_pylpnk_3e2zi8_4euq0x_40m1j2"]')

    #封装页面动作

    def login(self):
        self.open_browser()
        self.get(self.url)
        self.get_keys(self.account_loc,'1932521947@qq.com')
        self.get_keys(self.password_loc,'sq123!')
