from time import sleep

from selenium.webdriver.common.by import By

from Atid_Store.Locators.location import atid_demo_web, store_list_ul, men_head, men_yellow_shoes, add_to_cart, \
    click_men_item_in_cart, li
from Atid_Store.Test.Web.e2e import is_elemnet_exist


def test_men_shoe_price_greater_than_72_and_sale2():
    driver = super().website()
    web = driver.current_url
    assert web == atid_demo_web
    driver.find_element(By.XPATH, men_head).click()
    sleep(2)
    nav = driver.find_element(By.XPATH, store_list_ul)
    all_list = nav.find_elements(By.TAG_NAME, li)
    price = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[5]/div[2]/span[2]/ins[1]/span[1]/bdi[1]"
    for n in all_list:
        sale = is_elemnet_exist('onsale', n)
        Price = n.find_element(By.XPATH, price)
        a = Price.text
        casting = a[:-2]
        if sale == 'Sale!' and float(casting) > 72.00:  # casting
            sleep(5)
            n.click()
            sleep(5)
            break
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, men_yellow_shoes).click()
    cart = driver.title
    assert cart == "ATID Yellow Shoes – ATID Demo Store"
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(2)
    driver.find_element(By.XPATH, click_men_item_in_cart).click()
    sleep(2)
    cart = driver.title
    assert cart == "Cart – ATID Demo Store"
    driver.close()