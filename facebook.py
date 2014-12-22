# facebook interaction through webdriver

import urllib
import selenium
from selenium import webdriver

wd = webdriver.Firefox()
wd.get('https://www.facebook.com/')

email_entrance = wd.find_element_by_id('email')
password_entrance = wd.find_element_by_id('pass')

email_entrance.send_keys('reidjax@gmail.com')
password_entrance.send_keys('secret_password')

login_button = wd.find_element_by_id('loginbutton')

login_button.click()