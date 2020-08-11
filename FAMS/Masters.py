import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/FAMS/Masters"+timestamp
os.mkdir(path)

class FAMS_aMasters(unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://hublibrt.com:8089"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://hublibrt.com:8089")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_login_FAMS(self):
        driver = self.driver
        try:
            self.assertIn("Log in - FAMS", driver.title)
            time.sleep(3)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.User_name.clear()
            self.password.clear()

            try :
                self.User_name.send_keys("operator")
                self.password.send_keys("password")
                self.assertIn("Financial Accounting Management System", driver.page_source)
                print ("Validation of Master tab")
                self.submit = driver.find_element_by_xpath("//*[@class='btn btn-primary btn-group-justified']").click()
                time.sleep(10)
                self.menu = driver.find_element_by_xpath("//*[@class='menu-toggler']").click()
                time.sleep(4)
                self.masters = driver.find_element_by_xpath("//*[@data-original-title='Masters']").click()
                time.sleep(4)
                self.org = driver.find_element_by_xpath("//*[@data-original-title='Division']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_division" + timestamp + ".png")
                time.sleep(6)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Organization']")
                self.organization.click()
                driver.get_screenshot_as_file(path + "/" + "Masters_Organization" + timestamp + ".png")
                time.sleep(8)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Depot']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Depot" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Account']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Account" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Account Type']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Account_Type" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Bank']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Bank" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Tax']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Tax" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Fund Scheme']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Fund_Scheme" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Fund Agency']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Fund_Agency" + timestamp + ".png")
                time.sleep(4)
                self.organization = driver.find_element_by_xpath("//*[@data-original-title='Fund Project']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Masters_Fund_Project" + timestamp + ".png")
                time.sleep(4)
                print("Validation of FAMS Master tab is pass")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)