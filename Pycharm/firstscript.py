from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(30)
driver.get("http://facebook.com")
driver.maximize_window()
driver.implicitly_wait(30)

assert "chethan" in driver.title

username = driver.find_element_by_id("email")
password = driver.find_element_by_name("pass")
login = driver.find_element_by_id("loginbutton")

username.send_keys("chethanpintu@gmail.com")
password.send_keys("987654321")
login.click()

# driver.quit()
