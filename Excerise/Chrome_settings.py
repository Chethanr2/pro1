from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ChromeOptions = Options()
ChromeOptions.add_experimental_option("prefs",{"download.default_directory" : r"C:\Users\Chethan\Desktop\Adobe"})
driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe",chrome_options=ChromeOptions)

driver.get("http://nechubli.com:2001/#/")
driver.maximize_window()
time.sleep(10)

driver.find_element_by_id("UserName").send_keys("admin")
driver.find_element_by_id("Password").send_keys("admin@321")
driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']").click()

time.sleep(10)

driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/interface-cmp/div/form/div[2]/div/div/button").click()

time.sleep(60)

driver.quit()