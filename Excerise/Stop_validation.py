from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")



driver.get("http://hublibrt.com:2001")
driver.maximize_window()
driver.set_page_load_timeout(230)

print("Verifying the login page")
time.sleep(30)
#assertIn("VPSD System", driver.title)
driver.find_element_by_name("userID").send_keys('VPSD')
driver.find_element_by_name("password").send_keys('Vpsd@master@123')
time.sleep(3)
driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']").click()

time.sleep(55)
#assertIn("Vehicle Planning and Scheduling System", driver.page_source)
time.sleep(15)

driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/home-cmp/div/div[2]/div[1]/div/div[4]/a").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/stopmst-com/div[1]/div/div[1]/div[2]/div[7]/div/button").click()
time.sleep(15)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
records = driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/stopmst-com/div[1]/div/div[2]/div[2]/div/extended-grid-cmp/div[2]/div/div[2]").text
time.sleep(4)

print(records)
j = 0
for elm in records:
    j = j + 1
    if elm == ':':
        j = j + 1
        new_rec = records[j:]

print(new_rec)


driver.quit()