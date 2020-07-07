import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/Bussiness_rules"+timestamp
os.mkdir(path)

class VPSD_Bussiness_rules(unittest.TestCase):

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

            self.assertIn("VPSD System", self.driver.title)
            self.User_name = self.driver.find_element_by_id("UserName")
            self.password = self.driver.find_element_by_id("Password")
            self.submit = self.driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()

            self.User_name.send_keys("admin")
            self.password.send_keys("admin@321")
            self.submit.click()
            time.sleep(15)

            try:
                self.assertIn("Vehicle Planning and Scheduling System", self.driver.page_source)
                time.sleep(15)
            except AssertionError:
                print("Hitting wrong URL")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_login_VPSD(self):
        driver = self.driver
        print ("Validation of Bussiness Rules tab")
        self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Business Rule']").click()
        time.sleep(5)
        print("Validation of Bussiness Rules tab is pass")

    def test_printing(self):
        print("Testing the test suit")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)