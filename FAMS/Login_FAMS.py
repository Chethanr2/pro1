import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/FAMS/Login"+timestamp
os.mkdir(path)

class FAMS_aLogin(unittest.TestCase):

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
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Login" + timestamp + ".png")
                time.sleep(4)
                print("FAMS Login is successful")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)