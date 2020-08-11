from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

# Scroll windows by specifying the window position
# Scroll of window screen to specified location by giving the position
# driver.execute_script("window.scrollBy(0,1000)","")


# Scroll windows screen to specified location by giving the object of clicable element
map = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[49]/td[1]/img")

driver.execute_script("arguments[0].scrollIntoView();", map)
time.sleep(3)

driver.quit()