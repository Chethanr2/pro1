import unittest
from urllib.request import urlopen
from selenium import webdriver
import datetime
import time
import requests
#from HtmlTestRunner import HTMLTestRunner
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/login_tab"+timestamp
#os.mkdir(path)

class VPSD_aLogin(unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://hublibrt.com:2001"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://hublibrt.com:2001")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_login_VPSD(self):
        driver = self.driver
        try:
            print ("Verifying the login page")
            self.assertIn("VPSD System", driver.title)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.submit = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()

            try :
                self.User_name.send_keys('VPSD')
                self.password.send_keys('Vpsd@master@123')
                self.submit.click()
                time.sleep(5)
                self.assertIn("Vehicle Planning and Scheduling System", driver.page_source)
                time.sleep(15)
                #driver.get_screenshot_as_file(path+"/" + "VPSD_login_page" + timestamp + ".png")
                time.sleep(7)
                print("Login successful")
            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()