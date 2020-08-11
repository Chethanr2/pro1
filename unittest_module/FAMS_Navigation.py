import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests

class FAMS_NAVIGATION (unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://hublibrt.com:8089"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(30)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://hublibrt.com:8089")

        except requests.ConnectionError as e:
            print ("not connected :", e)

    def test_Login_check(self):
        driver = self.driver
        try:
            print ("In Test_FAMS_Login Page")
            self.assertIn("FAMS", driver.title)
            self.Financial_year = driver.find_element_by_id("FinancialYear")
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            submit = driver.find_element_by_xpath("//*[@class='btn btn-primary btn-group-justified']")
            self.User_name.clear()
            self.password.clear()
            try :
                self.User_name.send_keys("operator")
                self.password.send_keys("password")
                submit.click()
                self.assertIn("Dashboard - Finance and Accounting Management System", driver.title)
                time.sleep(5)
                driver.get_screenshot_as_file("G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/Login_page.png")
                time.sleep(3)
            except AssertionError:
                print ("Login failed : Invalid Username and Password")
            time.sleep(5)
        except AssertionError:
             print("Hitting wrong URL")

    def test_navigation_inside(self):
        print ("In Test_navigation_inside")
        driver = self.driver
        driver.find_element_by_xpath("//*[@class='menu-toggler']").click()
        driver.find_element_by_xpath("//li[contains(text(),'Masters')]").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()