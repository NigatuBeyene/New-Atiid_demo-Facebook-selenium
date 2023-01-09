from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Facebook.Locators.location import *
from Facebook.Test.BaseTest.base import *


class Testing(BaseTest):

    def test_valid_registation_all_requerments_are_field_correctly(self):  # 1
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("nigatu")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("beyene")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_invalid_firstname_field_NONE_but_all_requerments_are_field_correctly(self):  # 2
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("beyene")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_invalid_lastname_field_NONE_but_all_requerments_are_field_correctly(self):  # 3
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("nigatu")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_invalid_all_requerments_are_field_correctly_exept_incorrect_phone_number(self):  # 4
        # driver = webdriver.Chrome()
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("nigatu")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("beyene")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("8041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_invalid_all_requerments_are_field_correctly_exept_invalid_bith_date(self):  # 5
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("nigatu")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("beyene")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("62")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("30")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2045")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_valid_registation_all_requerments_are_field_correctly_exept_fistname_and_lastname_field_are_NONE(self):  # 6
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0533988041")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()

    def test_invalid_registation_all_requerments_are_field_correctly_exept_fistname_field_NONE_and_invalid_password(self):  # 7
        driver = super().facebookWeb()
        driver.get(facebookWebsite)
        driver.find_element(By.XPATH, creat_new_account).click()
        sleep(3)
        firstname = driver.find_element(By.XPATH, fistName)
        firstname.send_keys("")

        sleep(3)
        lastname = driver.find_element(By.XPATH, lastName)
        lastname.send_keys("beyene")

        sleep(3)
        phone = driver.find_element(By.XPATH, phoneNumber)
        phone.send_keys("0533988041")

        newpassword = driver.find_element(By.XPATH, new_password)
        newpassword.send_keys("0234")

        birth_day = driver.find_element(By.XPATH, birthday_day)
        birth_day.send_keys("12")
        sleep(3)

        birth_month = driver.find_element(By.XPATH, birthday_month)
        birth_month.send_keys("5")
        sleep(3)

        birth_year = driver.find_element(By.XPATH, birthday_year)
        birth_year.send_keys("2023")
        sleep(3)
        driver.find_element(By.XPATH, sign_up).click()

        sleep(5)
        driver.close()
