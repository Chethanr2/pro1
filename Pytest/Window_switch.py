from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://hublibrt.com:8089")
time.sleep(4)
driver.maximize_window()
driver.find_element_by_name("UserName").send_keys("Administrator")
driver.find_element_by_name("Password").send_keys("password")
time.sleep(4)
driver.find_element_by_xpath("//*[@id='loginForm']/form/input[2]").click()
time.sleep(10)

driver.find_element_by_xpath("//*[@id='header']/div/div[2]/ul[3]/li/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='sidenav']/div/ul/li[5]/a").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='sidenav']/div/ul/li[5]/ul/li[5]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='PageDiv']/form/div[1]/a").click()
time.sleep(5)
driver.switch_to_alert().accept()
time.sleep(5)

driver.quit()