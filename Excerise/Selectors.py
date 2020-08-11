from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")


driver.find_element(By.LINK_TEXT,"REGISTER").click()

time.sleep(5)
driver.quit()