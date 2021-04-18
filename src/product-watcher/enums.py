from enum import Enum


class LogIn(Enum):
    sign_in = '//*[@id="mainHeader"]/div/header/div[2]/div/div[3]/div[3]/div/div[1]/button'
    sign_in_menu = '/html/body/main/div[3]/div/div/ul/li[1]/a'
    amway_id_input = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/app-smart-id/div/app-form-field/div/input'
    password_input = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/password/div/div[2]/input'
    sign_in_btn = '/html/body/div/div/div/app-root/div/div[1]/div/app-signin/div/div/div/div/div/div/app-button/button'


class Home(Enum):
    url = 'https://www.amway.com/en_US/'
    search_bar = '/html/body/main/div[6]/div/header/div[3]/div/div[2]/div[1]/div/div/form/div/label/input'
    sign_out = '/html/body/main/div[3]/div/div/ul/li[11]/a'


class Product(Enum):
    product_name_xpath = '/html/body/main/div[11]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/div/h1/span'
    product_link = '/html/body/main/div[11]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/h3/a'
    availability = '/html/body/main/div[11]/div[2]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/span/span[2]'
