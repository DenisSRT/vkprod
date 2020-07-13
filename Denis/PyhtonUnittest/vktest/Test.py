from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



def auth_test():
    driver = webdriver.Chrome('C:\chromedriver.exe')
    driver.get("https://vk.com/")
    elem = driver.find_element_by_id("index_email")
    elem.send_keys("89179908475")
    elem = driver.find_element_by_id("index_pass")
    elem.send_keys("geirbyf48")
    elem.send_keys(Keys.RETURN)
    driver.close()

auth_test()

