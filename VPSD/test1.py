import random
import datetime
import unittest
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests
import datetime
import os
import random
date = datetime.datetime.now().strftime("%d-%m-%Y")

driver = webdriver.Chrome()
driver.set_page_load_timeout(120)
driver.maximize_window()
driver.implicitly_wait(60)
driver.get("http://hublibrt.com:8089")

time.sleep(3)
User_name = driver.find_element_by_id("UserName")
password = driver.find_element_by_id("Password")
User_name.clear()
password.clear()


User_name.send_keys("operator")
password.send_keys("password")
print("Validation of Master tab")
submit = driver.find_element_by_xpath("//*[@class='btn btn-primary btn-group-justified']").click()
time.sleep(10)
menu = driver.find_element_by_xpath("//*[@class='menu-toggler']").click()
time.sleep(4)
customer = driver.find_element_by_xpath("//*[@data-original-title='Customer']").click()
time.sleep(8)
sales_order = driver.find_element_by_xpath("//*[@data-original-title='Sales Order']").click()
time.sleep(4)
new_sales_order = driver.find_element_by_xpath("//*[@class='btn btn-primary show-modal']").click()
time.sleep(4)


driver.quit()