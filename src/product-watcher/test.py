# # pip install selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import datetime
import config


# variables
wait_time = 5
product_name = 'Artistry-Ideal-Radiance'
txt_script = 'send-message.applescript'
driver_path = '../web-driver/chromedriver'
product_xpath = '/html/body/main/div[11]/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/span/span[2]'
product_url = 'https://www.amway.com/en_US/Artistry-Ideal-Radiance%26trade%3B-Illuminating-CC-Cream---Light-Medium-p-118207?searchTerm=light%20medium'


print('Watching for {} \n'.format(product_name))
print('URL: {} \n'.format(product_url))

# Set Setting for chrome
chrome_options = Options()
# chrome_options.add_argument('--headless') # Headless being off is needed for login
DRIVER = webdriver.Chrome(driver_path, options=chrome_options)

# ================== Functions ==================


def login():
    DRIVER.get('https://www.amway.com/en_US/')

    sign_in = '//*[@id="mainHeader"]/div/header/div[2]/div/div[3]/div[3]/div/div[1]/button'
    DRIVER.find_element_by_xpath(sign_in).click()

    sign_in_menu = '/html/body/main/div[3]/div/div/ul/li[1]/a'
    DRIVER.find_element_by_xpath(sign_in_menu).click()

    time.sleep(3)

    amway_id_input = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/app-smart-id/div/app-form-field/div/input'
    amway_id_input = DRIVER.find_element_by_xpath(amway_id_input)
    amway_id_input.send_keys(config.email)

    password_input = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/password/div/div[2]/input'
    password_input = DRIVER.find_element_by_xpath(password_input)
    password_input.send_keys(config.password)

    sign_in_btn = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/app-button/button'
    DRIVER.find_element_by_xpath(sign_in_btn).click()


login()
