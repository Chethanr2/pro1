from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")

driver.get("http://hublibrt.com:8089")
driver.maximize_window()
time.sleep(3)

Usr = driver.find_element_by_id("UserName")
PSW = driver.find_element_by_id("Password")

Usr.send_keys("Administrator")
PSW.send_keys("password")

submit = driver.find_element_by_xpath("//*[@id='loginForm']/form/input[2]").click()
time.sleep(4)

driver.find_element_by_xpath("//*[@class='menu-toggler']").click()
time.sleep(3)
#masters = driver.find_element_by_xpath("//*[@data-original-title='Masters']").click()
#time.sleep(4)
Customer = driver.find_element_by_xpath("//*[@id='sidenav']/div/ul/li[4]/a")
Customer.click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='sidenav']/div/ul/li[4]/ul/li[2]/a").click()
time.sleep(2)

New_Cust = driver.find_element_by_xpath("//*[@id='sidenav']/div/ul/li[4]/ul/li[1]/a")
New_Cust.click()
time.sleep(6)

code = driver.find_element_by_xpath("//*[@id='CusCode']")
code.clear()
code.send_keys("Cut02")
time.sleep(2)

cust_name = driver.find_element_by_xpath("//*[@id='CusName']")
cust_name.clear()
cust_name.send_keys("Volvo")
time.sleep(2)

Phone_no = driver.find_element_by_xpath("//*[@id='Phone']")
Phone_no.clear()
Phone_no.send_keys("0999900007")

Email_add = driver.find_element_by_xpath("//*[@id='Email']")
Email_add.clear()
Email_add.send_keys("hdbrts@gmail.com")
time.sleep(4)

ContPer = driver.find_element_by_name("ContactPerson")
ContPer.send_keys("Biradar")
time.sleep(2)

dropd = driver.find_element_by_xpath("//*[@id='Type_chosen']/a/div/b")
dropd.click()
time.sleep(2)
sel = driver.find_element_by_xpath("//*[@id='Type_chosen']/div/ul/li[2]")
sel.click()
time.sleep(2)

Bill_inform = driver.find_element_by_xpath("//*[@id='form0']/div[1]/ul/li[2]/a")
Bill_inform.click()
time.sleep(4)

BillAdd = driver.find_element_by_name("Billadd")
BillAdd.send_keys("Hubli brts")
time.sleep(2)

gstNo = driver.find_element_by_name("GSTNo")
gstNo.send_keys("RFTYUI8987")
time.sleep(2)

panNo = driver.find_element_by_name("PanNo")
panNo.send_keys("AHSPC0093L")
time.sleep(2)

ShipAdd = driver.find_element_by_xpath("//*[@id='form0']/div[1]/ul/li[3]/a")
ShipAdd.send_keys("Hubli BRTS")
time.sleep(3)

driver.quit()