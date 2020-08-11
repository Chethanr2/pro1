from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame("packageListFrame")

driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(4)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("ChromeDriver").click()
time.sleep(4)

driver.quit()