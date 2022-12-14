from selenium import webdriver


class BasePage:
    def __init__(self):
        self.wd = None

    def open_browser(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)

    def get(self, url):
        self.wd.get(url)

    def locator_element(self, args):
        return self.wd.find_element(*args)

    def get_keys(self, args, value):
        self.locator_element(args).send_keys(value)

    def click(self, args):
        self.locator_element(args).click()

    #鼠标悬浮
    def moveto_element(self, args):
        self.moveto_element(args).perform()
