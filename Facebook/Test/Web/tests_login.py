from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Facebook.Locators.location import *
from Facebook.Test.BaseTest.base import *


class Testing(BaseTest):

    def test_login_valid_using_correct_userName_and_password(self):  # correct user and password
        driver = super().facebookWeb()
        web = driver.current_url
        assert web == facebookWebsite
        driver.get(facebookWebsite)
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("Shuki Ruki")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("Post567&")
        driver.find_element(By.XPATH, login).click()
        sleep(10)
        super().tear_down()

    def test_login_invalid_using_NONE_user_field_and_correct_password(self):  # incorrect user and correct password

        driver = super().facebookWeb()
        facebook = driver.get(facebookWebsite)
        q = driver.current_url
        assert q == facebook
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("Post567&")
        driver.find_element(By.XPATH, login).click()
        sleep(5)
        error = driver.find_element(By.XPATH, error_message).text
        assert error == "Find your account and log in."
        sleep(10)
        super().tear_down()

    def test_login_invalid_using_correct_username_and_incorrect_password_invalid_field_none(self):  # correct username  and password
        driver = super().facebookWeb() # ###
        driver.get(facebookWebsite)
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("Shuki Ruki")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("")
        driver.find_element(By.XPATH, ).click()
        sleep(4)

        error = driver.find_element(By.XPATH, error_message).text
        assert error == " Forgotten password?"
        sleep(10)
        super().tear_down()

    def test_login_invalid_with_both_username_and_password_field_none(self):  # both user and password are incorrect
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("")
        driver.find_element(By.XPATH, login).click()
        sleep(5)
        error = driver.find_element(By.XPATH, error_message).text
        assert error == "Find your account and log in."
        sleep(10)
        super().tear_down()

    def test_login_invalid_using_incorrect_username_and_NONE_password(self):  # incorrect username and NONE password
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("3456789oi")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("")
        driver.find_element(By.XPATH, login).click()
        sleep(4)
        error = driver.find_element(By.XPATH, error_message).text
        assert error == " Forgotten password?"
        sleep(5)
        super().tear_down()

    def test_login_invalid_with_both_username_and_password_field_are_invalid(self):  # both_username_and_password_field_are_invalid
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        fb_user = driver.find_element(By.XPATH, userName)
        fb_user.send_keys("ertyuio")
        fb_password = driver.find_element(By.XPATH, password)
        fb_password.send_keys("4zxfdtr64")
        driver.find_element(By.XPATH, login).click()
        sleep(5)
        error = driver.find_element(By.XPATH, error_message).text
        assert error == "Find your account and log in."
        sleep(10)
        super().tear_down()
