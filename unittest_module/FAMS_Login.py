import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
from HtmlTestRunner import HTMLTestRunner

class FAMSLogin(unittest.TestCase):

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

    def test_login_FAMS(self):
        driver = self.driver
        try:
            print ("IN test_login_fams")
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
                #self.assertIn("Dashboard - Finance and Accounting Management System", driver.title)
                assert "Invalid login attempt." not in driver.page_source
                time.sleep(5)
                driver.get_screenshot_as_file("G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/Login_page.png")
                time.sleep(3)
            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()