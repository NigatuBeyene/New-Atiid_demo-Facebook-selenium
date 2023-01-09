from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from Atid_Store.Locators.location import *


def test_store_product_in_cart():
    driver = webdriver.Chrome()
    driver.get(atid_demo_web)
    driver.find_element(By.XPATH, store_head).click()
    sleep(2)
    driver.find_element(By.XPATH, store_body).click()
    sleep(2)
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(2)
    element = driver.find_element(By.XPATH, store_item_name).text
    sleep(4)
    assert element == "Black Over-the-shoulder Handbag"
    driver.close()


def test_men_product_in_cart():
    driver = webdriver.Chrome()
    driver.get(atid_demo_web)
    driver.find_element(By.XPATH, men_head).click()
    sleep(4)
    driver.find_element(By.XPATH, men_blue_shoes).click()
    sleep(4)
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(4)
    driver.find_element(By.XPATH, men_body).click()
    element = driver.find_element(By.XPATH, men_item_in_cart).text
    sleep(4)
    assert element == "ATID Blue Shoes"
    driver.close()


def test_women_product_in_cart():
    driver = webdriver.Chrome()
    driver.get(atid_demo_web)
    driver.find_element(By.XPATH, women_head).click()
    sleep(4)
    driver.find_element(By.XPATH, women_product_name).click()
    sleep(4)
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(4)
    driver.find_element(By.XPATH, women_body).click()
    element = driver.find_element(By.XPATH, women_item_in_cart).text
    sleep(4)
    assert element == "Basic Gray Jeans"
    driver.close()


def test_accecablity():
    driver = webdriver.Chrome()
    driver.get(atid_demo_web)
    driver.find_element(By.XPATH, accecablity_head).click()
    sleep(4)
    driver.find_element(By.XPATH, accecablity_product_name).click()
    sleep(4)
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(4)
    driver.find_element(By.XPATH, accecablity_body).click()
    element = driver.find_element(By.XPATH, accecablity_item_in_cart).text
    sleep(4)
    assert element == "Black Over-the-shoulder Handbag"
    driver.close()


def test_Coupon_Code():
    driver = webdriver.Chrome()
    driver.get(atid_demo_web)
    driver.find_element(By.XPATH, men_head).click()
    driver.find_element(By.XPATH, men_blue_shoes).click()
    driver.find_element(By.XPATH, add_to_cart).click()
    driver.find_element(By.XPATH, men_body).click()
    element = driver.find_element(By.XPATH, men_item_in_cart).text
    assert element == "ATID Blue Shoes"
    coupon_code = driver.find_element(By.XPATH, coupon_code_field)
    coupon_code.send_keys("nige")
    driver.find_element(By.XPATH, apply_coupon).click()
    sleep(5)
    error = driver.find_element(By.XPATH, error_message).text

    assert error == 'Coupon "nige" does not exist!'
    sleep(10)
    driver.close()
