import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/Reports"+timestamp
os.mkdir(path)

class VPSD_gReports(unittest.TestCase):

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
            self.assertIn("VPSD System", driver.title)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.submit = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()

            try :
                self.User_name.send_keys("VPSD")
                self.password.send_keys("Vpsd_master@321")
                self.submit.click()
                self.assertIn("Vehicle Planning and Scheduling System", driver.page_source)
                time.sleep(15)
                print ("Validation of Reports tab")
                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(15)

                # To check for Reports of Form II masters in the application
                driver.find_element_by_link_text('Form II Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Form_II_report"+timestamp+".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for Form IV report in the application
                driver.find_element_by_link_text('Form IV Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Form_IV_reports" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for form V reports in the application
                driver.find_element_by_link_text('Form V Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Form_V_reports" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for Time table report in the application
                driver.find_element_by_link_text('Time Table Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Time_Table_Report" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for Distance report in the application
                driver.find_element_by_link_text('Distance Report - Schedule').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Distance_Report_Schedule" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for Division level reports in the application
                driver.find_element_by_link_text('Division Level Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Division_Level_Report" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check for Deport level report in the application
                driver.find_element_by_link_text('Depot Level Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Depot_Level_Report" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check Vehicle schedule report in the application
                driver.find_element_by_link_text('Vehicle Schedule Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Vehicle_Schedule_Report" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='fa fa-file-o']")
                self.submit1.click()
                time.sleep(5)

                # To check Stop level report in the application
                driver.find_element_by_link_text('Stop Level Report').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "Stop_Level_Report" + timestamp + ".png")
                time.sleep(4)

                print("Validation of route tab is pass")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)