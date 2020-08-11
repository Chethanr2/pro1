from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

# TO scroll the window to 1000 position on the window
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(4)

# To scroll the window to a particular element on the page
flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[66]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(4)

# To scroll the window to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(6)

driver.quit()