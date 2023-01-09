from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Facebook.Locators.location import *
from Facebook.Test.BaseTest.base import *


class Testing(BaseTest):

    def test_valid_forgetpassword(self):
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, forgetPassword).click()

        driver.find_element(By.XPATH, finding_account).click()
        fb_recover = driver.find_element(By.XPATH, your_email)
        fb_recover.send_keys("example@gmail.com")
        driver.find_element(By.XPATH, submit).click()
        sleep(5)
        super().teardown()

    def test_invalid_forgetpassword_incorrect_gmail(self):
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, forgetPassword).click()

        driver.find_element(By.XPATH, finding_account).click()
        fb_recover = driver.find_element(By.XPATH, your_email)
        fb_recover.send_keys("example@om")
        driver.find_element(By.XPATH, submit).click()
        sleep(5)
        super().teardown()

    def test_invalid_forgetpassword_NONE_gmail(self):
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, forgetPassword).click()
        driver.find_element(By.XPATH, finding_account).click()
        fb_recover = driver.find_element(By.XPATH, your_email)
        fb_recover.send_keys(" ")
        driver.find_element(By.XPATH, submit).click()
        sleep(5)
        super().teardown()


