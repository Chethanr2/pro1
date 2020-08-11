from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")

driver.find_element_by_link_text("org.openqa.selenium").click()

time.sleep(4)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")

driver.find_element_by_link_text("OutputType").click()
time.sleep(4)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")

driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()

time.sleep(4)

driver.quit()