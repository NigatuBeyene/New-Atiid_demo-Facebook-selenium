
from selenium import webdriver
from Atid_Store.Locators.location import *


class BaseTest():
    driver = webdriver.Chrome()

    def website(self):
        self.driver.get(atid_demo_web)
        self.driver.maximize_window()
        return self.driver

    def tear_down(self):
        self.driver.quit()
        self.driver.close()
