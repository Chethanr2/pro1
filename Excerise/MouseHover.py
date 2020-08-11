from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

time.sleep(4)

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermgt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
usr = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

mouseactions = ActionChains(driver)

mouseactions.move_to_element(admin).move_to_element(usermgt).move_to_element(usr).click().perform()
time.sleep(4)

driver.execute_script("window.scrollBy(0,1000)","")

time.sleep(4)

driver.quit()