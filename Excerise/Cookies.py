from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("https://www.flipkart.com/")
time.sleep(4)

cookies = driver.get_cookies()

print(len(cookies))
print(cookies)
time.sleep(4)

# Add cookies in to cache

cookie = {'name': 'MyCookie', 'value': '123456'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)

driver.delete_cookie('MyCookie')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
time.sleep(2)

driver.quit()
