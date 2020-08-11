from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("http://www.hublibrt.com:2001/")

driver.implicitly_wait(20)
userName = driver.find_element_by_id("UserName")
Password = driver.find_element_by_id("Password")

userName.send_keys("VPSD")
Password.send_keys("Vpsd@master@123")

driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']").click()

time.sleep(20)

driver.find_element_by_xpath("//*[@class='btn btn-default btn-block green_btn']").click()

time.sleep(4)


time.sleep(4)
driver.quit()




