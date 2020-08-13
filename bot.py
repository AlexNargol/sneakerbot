from config import keys
from selenium import webdriver
import time


def order(k):

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(k['product_url'])

    driver.find_element_by_xpath('//*[@id="addToCart-product-template"]').click()

    time.sleep(7)
    #driver.find_element_by_xpath('// *[ @ id = "supreme-xxl-hooded-sweatshirt"]')
    driver.switch_to.frame("swell-popup")
    driver.find_element_by_xpath('//*[@id="swell-popup-close-x"]/i').click()

    driver.switch_to.parent_frame()
    driver.find_element_by_xpath('// *[ @ id = "ajaxifyCart"] / form / div[2] / div / div[2] / button').click()
    driver.find_element_by_xpath('//*[@id="checkout_email_or_phone"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="checkout_buyer_accepts_marketing"]').click()
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys(k["first_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys(k["last_name"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys(k["postcode"])
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys(k["phone_number"])
    driver.find_element_by_xpath('//*[ @ id = "continue_button"]').click()
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()
    driver.find_element_by_xpath('//*[@id="section--tip-presets"]').click()
    time.sleep(30)


if __name__ == '__main__':
    order(keys)
