# RFP- 1174 : Application shall have feature to capture trip/schedule wise revenue kilometers

import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import pandas as pd
import datetime
import os
import shutil
from selenium.webdriver.support.ui import Select

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/VPSD/RFP_Execution/Screenshots"+timestamp
os.mkdir(path)

class RFP_1174(unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://nechubli.com:2001"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://nechubli.com:2001")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_login_VPSD(self):
        driver = self.driver
        try:
            self.assertIn("VPSD System", driver.title)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.submit = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()

            try:
                self.User_name.send_keys("admin")
                self.password.send_keys("admin@321")
                self.submit.click()
                self.assertIn("Vehicle Planning and Scheduling System", driver.page_source)
                time.sleep(20)

                driver.find_element_by_xpath("//*[@class='btn btn-default btn-block teal_btn']").click()
                time.sleep(10)
                driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                time.sleep(5)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.get_screenshot_as_file(path + "/" + "Revenue KM" + timestamp + ".png")
                time.sleep(5)
                driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/vehicleschedule/div[2]/div/div[2]/div/extended-grid-cmp/div[1]/div[2]/ul/li/span[1]/i").click()
                time.sleep(10)
                print("Vehicle schedule details are downloaded in Download folder with timestamp")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()