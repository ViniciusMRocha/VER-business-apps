# pip install selenium
import os
import time
import datetime
import config
import enums
import smtplib

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

SEND_MESSAGE_SCRIPT = '../../scripts/send-message.applescript'
RERUN_WAIT_TIME = 5
PRODUCTS = {'124936': 'Collagen Shots',
            '300325': 'CBD Pro Sample',
            '124557': 'Focus Shot'}


# Set Setting for chrome
chrome_options = Options()
DRIVER = webdriver.Chrome('../web-driver/chromedriver',
                          options=chrome_options)


def login():
    DRIVER.get('https://www.amway.com/en_US/')

    time.sleep(1)
    DRIVER.find_element_by_xpath(enums.LogIn.sign_in.value).click()

    time.sleep(1)
    DRIVER.find_element_by_xpath(enums.LogIn.sign_in_menu.value).click()

    time.sleep(5)
    amway_id_input = DRIVER.find_element_by_xpath(enums.LogIn.amway_id_input.value)
    amway_id_input.click()
    amway_id_input.send_keys(config.email)

    password_input = DRIVER.find_element_by_xpath(enums.LogIn.password_input.value)
    password_input.click()
    password_input.send_keys(config.password)

    sign_in_btn = enums.LogIn.sign_in_btn.value
    DRIVER.find_element_by_xpath(sign_in_btn).click()
    time.sleep(5)


def logout():
    time.sleep(1)
    DRIVER.find_element_by_xpath(enums.LogIn.sign_in.value).click()

    time.sleep(1)
    DRIVER.find_element_by_xpath(enums.Home.sign_out.value).click()


def get_product_info(item_id):

    # Send SKU to the search bar
    search_bar = DRIVER.find_element_by_xpath(enums.Home.search_bar.value)
    search_bar.click()
    search_bar.send_keys(item_id)
    search_bar.send_keys(Keys.RETURN)

    # Click on the first product link
    time.sleep(3)
    product_link = DRIVER.find_element_by_xpath(enums.Product.product_link.value)
    product_link.click()

    # Get the product availability
    time.sleep(3)
    availability = DRIVER.find_element_by_xpath(enums.Product.availability.value).text

    return {'id': item_id, 'availability': availability}


def send_text_as_email(number, carrier, from_email, from_email_pass, message):
    """ Used for sending SMS to non iPhone users """
    # Not implemented yet

    carriers = {'att': '@mms.att.net',
                'verizon': '@vtext.com',
                'tmobile': ' @tmomail.net',
                'sprint': '@page.nextel.com'}

    contact_carrier = carriers[carrier]
    to_number = f'{number}{contact_carrier}'
    subject = 'Subject: Product Update:\n'
    conn = smtplib.SMTP_SSL('smtp.mail.gmail.com', 465)
    conn.ehlo()
    conn.login(from_email, from_email_pass)
    conn.sendmail(from_email, to_number, subject + message)
    conn.quit()


def send_notification(sku, product_name):
    # Get contact list form config
    contact_list = config.contact_list
    # Iterate over each contact
    for name in contact_list:
        # Get number
        number = contact_list[name]
        # Compose product link variable
        product_link = f'https://www.amway.com/en_US/search/?text={sku}'
        # Form message
        message = f'Hey {name}, {product_name} is back in stock\n{product_link}'
        # Form the command to send message
        command = f'osascript {SEND_MESSAGE_SCRIPT} {number} "{message}"'
        # Execute the send message command
        os.system(command)

        print(f'Sending message to {name} on number {number}')


def check_report(report):
    # Check the report and send a text for the available ones
    for sku in report:
        # Check if sku status is in stock
        if report[sku] == 'In Stock':
            # Get product name
            product_name = PRODUCTS[sku]
            # Removed sku that was already communicated to be in stock
            PRODUCTS.pop(sku)
            # Notify about the product being in stock
            send_notification(sku, product_name)


def run_app():
    """ Handler """
    try:
        while PRODUCTS:
            # Log in to the website
            login()

            # Get product status
            report = {}
            for item_id in PRODUCTS:
                # Get product availability
                availability = get_product_info(item_id)
                report.update({availability['id']: availability['availability']})

            # Evaluate report and send messages
            check_report(report)

            print(datetime.datetime.now())
            print('Current Report')
            print(report)
            print('--------------------')

            # Wait time for the next check
            logout()
            time.sleep(RERUN_WAIT_TIME)

        if not PRODUCTS:
            # Notify that all the products were evaluated
            message = 'All product were reported. Product watch will terminate'
            command = f'osascript ../../scripts/{SEND_MESSAGE_SCRIPT} {config.support_number} "{message}"'
            os.system(command)

    except Exception:
        # Notify that there was an exception
        message = 'There was an issue with the product watcher'
        command = f'osascript ../../scripts/{SEND_MESSAGE_SCRIPT} {config.support_number} "{message}"'
        os.system(command)
        raise

    finally:
        # Close browser
        DRIVER.quit()
        print('======== The End ========')


if __name__ == "__main__":
    run_app()
