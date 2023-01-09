from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver


class BaseTest():
    driver = webdriver.Chrome()

    def facebookWeb(self):
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        self.driver.quit()
        self.driver.close()


