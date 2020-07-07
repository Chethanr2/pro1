import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/User_management"+timestamp
os.mkdir(path)

class VPSD_hUser_management(unittest.TestCase):

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
                print ("Validation of User management tab")
                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='User Management']").click()
                time.sleep(5)

                # To check for Users in the application
                driver.find_element_by_link_text('User').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"users"+timestamp+".png")
                time.sleep(4)

                self.submit2 = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                time.sleep(4)
                driver.get_screenshot_as_file(path + "/" + "users_list" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='User Management']").click()
                time.sleep(5)

                # To check for Roles in the application
                driver.find_element_by_link_text('Role').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Role" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='User Management']").click()
                time.sleep(5)

                # To check for Departments in the application
                driver.find_element_by_link_text('Department').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Department" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='User Management']").click()
                time.sleep(5)

                # To check for Organisation in the application
                driver.find_element_by_link_text('Organisation').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Organisation" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='User Management']").click()
                time.sleep(5)

                # To check for Screen Access in the application
                driver.find_element_by_link_text('Screen Access').click()

                print("Validation of User management is pass")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
            time.sleep(4)
            driver.get_screenshot_as_file(path +"/"+ "Screen Access" + timestamp + ".png")
            time.sleep(4)
            print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)