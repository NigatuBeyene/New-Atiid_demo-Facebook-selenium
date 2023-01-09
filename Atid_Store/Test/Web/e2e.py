# 1. Write 5 Test Cases E2E

from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from Atid_Store.Test.BaseTest.base import *
from Atid_Store.Test.Web import tests

from Atid_Store.Test.Web import is_elemnet_exist
# E2E adding to cart

tests.test_accecablity()
tests.test_men_product_in_cart()
tests.test_Coupon_Code()
tests.test_women_product_in_cart()
tests.test_store_product_in_cart()


# E2E from login to check out end proceed

def is_elemnet_exist(param, n):
    pass


class Test(BaseTest):
    def test_proceed_to_checkout_end_to_end(BaseTest):
        # driver = webdriver.Chrome()
        driver = super().website()
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
        driver.find_element(By.XPATH, add_to_cart).click()  # add cart
        sleep(2)
        driver.find_element(By.XPATH, view_cart).click()  # view cart
        sleep(2)
        driver.find_element(By.XPATH, proceed_to_checkout).click()
        firstname_P = driver.find_element(By.XPATH, fist_name)  # fist name
        firstname_P.send_keys("nigatu")
        sleep(2)
        lastname_P = driver.find_element(By.XPATH, last_name)  # lastname
        lastname_P.send_keys("beyene")
        sleep(2)
        campany_P = driver.find_element(By.XPATH, companyname)  # companyname
        campany_P.send_keys("atid demo")
        sleep(2)
        driver.find_element(By.XPATH, country).click()  # county
        sleep(2)
        driver.find_element(By.XPATH, select_country)  # select country
        sleep(2)
        driver.find_element(By.XPATH, count).click()
        sleep(2)
        driver.find_element(By.XPATH, house).click()
        sleep(2)
        driver.find_element(By.XPATH, section).click()
        sleep(2)
        postcode = driver.find_element(By.XPATH, street_address_house)  # Street address
        postcode.send_keys("safat")
        sleep(2)
        postcode = driver.find_element(By.XPATH, postcodes)
        postcode.send_keys("0987645")
        sleep(2)
        postcode = driver.find_element(By.XPATH, zip)  # Postcode / ZIP
        postcode.send_keys("234567")
        sleep(2)
        postcode = driver.find_element(By.XPATH, city)  # city
        postcode.send_keys("jerusalem")
        sleep(2)
        phones = driver.find_element(By.XPATH, phone)  # phone numbers
        phones.send_keys("098765454")
        sleep(2)
        email_1 = driver.find_element(By.XPATH, email_address)  # email
        email_1.send_keys("beyenenigatu@gmail.com")
        sleep(2)
        driver.find_element(By.XPATH, place_order).click()  # place_order
        super().tear_down()

    def test_contact_us_e2e(BaseTest):
        driver = super().website()
        driver.get(atid_demo_web)
        current_web = driver.current_url
        assert current_web == atid_demo_web
        driver.find_element(By.XPATH, contact_head).click()
        contact_link = 'Contact Us – ATID Demo Store'
        assert contact_link == driver.title
        names = driver.find_element(By.XPATH, name)
        names.send_keys("nigatu")
        sleep(2)
        subjects = driver.find_element(By.XPATH, subject)
        subjects.send_keys("Appreciation!!")
        sleep(2)
        emails = driver.find_element(By.XPATH, email)
        emails.send_keys("example@gmail.com")
        sleep(2)
        messages = driver.find_element(By.XPATH, message)
        messages.send_keys(my_message)
        sleep(2)
        driver.find_element(By.XPATH, send).click()
        sleep(2)
        responces = driver.find_element(By.XPATH, responce).text
        assert responces == text
        super().tear_down()

    # 2.	Add to the cart just the product with sale & the original price > 72.00 (Bonus - Add all the products to the cart)

    def test_men_shoe_price_greater_than_72_and_sale1(self):

        driver = super().website()
        driver.get(atid_demo_web)
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, men_head).click()
        sleep(2)
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        price = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/ul[1]/li[5]/div[2]/span[2]/ins[1]/span[1]/bdi[1]"
        for n in all_list:
            saling = is_elemnet_exist('onsale', n)
            Price = n.find_element(By.XPATH, price)
            a = Price.text
            casting = a[:-2]
            if saling == 'Sale!' and float(casting) > 72.00:  # casting
                sleep(5)
                n.click()
                sleep(5)
                break
        driver.implicitly_wait(5)
        cart = driver.title
        # assert cart == "ATID Blue Shoes – ATID Demo Store"
        assert cart == "Men – ATID Demo Store"
        driver.find_element(By.XPATH, add_to_cart).click()
        sleep(2)
        driver.find_element(By.XPATH, click_men_item_in_cart).click()
        sleep(2)
        cart = driver.title
        assert cart == "Cart – ATID Demo Store"
        # super().tear_down()
        # driver.close()

    def is_elemnet_exist(text, webElemnet):
        try:
            return webElemnet.find_element(By.CLASS_NAME, text).text
        except NoSuchElementException:
            return ' '

    def test_men_shoe_price_greater_than_72_and_sale2(BaseTest):
        driver = super().website()
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, men_head).click()
        sleep(2)
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        sleep(5)
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(5)
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
        cart = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/h1[1]")
        assert cart.text == "Cart"
        super().tear_down()

    def is_elemnet_exist(text, webElemnet):
        try:
            return webElemnet.find_element(By.CLASS_NAME, text).text
        except NoSuchElementException:
            return ' '

    def test_women_product_price_greater_than_72_and_sale3(BaseTest):
        driver = super().website()
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, women_head).click()
        sleep(2)
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        for n in all_list:
            if n.text == 'Blue Denim Shorts':
                n.click()
                sleep(4)
                break
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, women_product_name1).click()
        cart = driver.title
        assert cart == "Blue Denim Shorts – ATID Demo Store"
        driver.find_element(By.XPATH, add_to_cart).click()
        sleep(2)
        driver.find_element(By.XPATH, click_women_item_in_cart).click()
        sleep(2)
        cart = driver.find_element(By.XPATH, cart_xpath)
        assert cart.text == "Cart"
        super().tear_down()

    def test_women_product_price_greater_than_72_and_sale4(BaseTest):
        driver = super().website()
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, women_head).click()  # women
        sleep(2)
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        for n in all_list:
            if n.text == 'Lemons Tshirt':
                n.click()
                sleep(4)
                break
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, next_page).click()  # next page
        driver.find_element(By.XPATH, women_product_name2).click()
        cart = driver.title
        assert cart == "Lemons Tshirt – ATID Demo Store"
        driver.find_element(By.XPATH, add_to_cart).click()
        sleep(2)
        driver.find_element(By.XPATH, click_women_item_in_cart).click()
        sleep(2)
        cart = driver.find_element(By.XPATH, cart_xpath)
        assert cart == "Cart"
        super().tear_down()

    def test_accessories_product_price_greater_than_72_and_sale4(BaseTest):  ########
        driver = super().website()
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, accecablity_head).click()  # Accessories
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        for n in all_list:
            if n.text == 'Bright Gold Purse With Chain':
                n.click()
                sleep(4)
                break

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, accecablity_select_item1).click()
        cart = driver.title
        assert cart == "Bright Gold Purse With Chain – ATID Demo Store"
        driver.find_element(By.XPATH, add_to_cart).click()
        sleep(2)
        driver.find_element(By.XPATH, click_accecablity_item_in_cart).click()
        sleep(2)
        cart = driver.find_element(By.XPATH, cart_xpath)
        assert cart == "Cart"
        super().tear_down()

    # 3.	In " Our Best Sellers" Section add only the products with 5-star rank

    def test_accessories_product_has_five_Stars(BaseTest):
        driver = super().website()
        web = driver.current_url
        assert web == atid_demo_web
        driver.find_element(By.XPATH, accecablity_head).click()  # Accessories
        nav = driver.find_element(By.XPATH, store_list_ul)
        all_list = nav.find_elements(By.TAG_NAME, li)
        for n in all_list:
            rate = n.find_element(By.CLASS_NAME, "rating")
            if rate.text == 5.00:
                n.click()
                sleep(4)
                break
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, accecablity_select_item).click()
        cart = driver.title
        assert cart == "Boho Bangle Bracelet – ATID Demo Store"
        driver.find_element(By.XPATH, add_to_cart).click()
        sleep(2)
        driver.find_element(By.XPATH, click_accecablity_item_in_cart).click()
        sleep(2)
        cart = driver.title
        assert cart == "Cart – ATID Demo Store"
        super().tear_down()

    # 4.	Send Question to the site admin via Contact Us screen (Bonus)

    def test_contact_us(BaseTest):
        driver = super().website()
        current_web = driver.current_url
        assert current_web == atid_demo_web
        driver.find_element(By.XPATH, contact_head).click()
        contact_link = 'Contact Us – ATID Demo Store'
        assert contact_link == driver.title
        names = driver.find_element(By.XPATH, name)
        names.send_keys("nigatu")
        sleep(2)
        subjects = driver.find_element(By.XPATH, subject)
        subjects.send_keys("Appreciation!!")
        sleep(2)
        emails = driver.find_element(By.XPATH, email)
        emails.send_keys("example@gmail.com")
        sleep(2)
        messages = driver.find_element(By.XPATH, message)
        messages.send_keys(my_message)
        sleep(2)
        driver.find_element(By.XPATH, send).click()
        sleep(2)
        responses = driver.find_element(By.XPATH, responce).text
        assert responses == text
        super().tear_down()
