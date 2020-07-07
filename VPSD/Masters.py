import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/Masters"+timestamp
os.mkdir(path)

class VPSD_fMasters(unittest.TestCase):

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
                print ("Validation of Masters tab")
                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(15)

                # To check for Master of stop type in the application
                driver.find_element_by_link_text('Stop Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Stop_type_master"+timestamp+".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of Route type in the application
                driver.find_element_by_link_text('Route Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Route_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of service type in the application
                driver.find_element_by_link_text('Service Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Service_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of Sector/Line type in the application
                driver.find_element_by_link_text('Sector/Line Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+"Sector_line_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of station type in the application
                driver.find_element_by_link_text('Station Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Station_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of Route category type in the application
                driver.find_element_by_link_text('Route Category Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Route_category_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check for Master of Route variant type in the application
                driver.find_element_by_link_text('Route Variant Type').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path +"/"+ "Route_variant_type_master" + timestamp + ".png")
                time.sleep(4)

                self.submit1 = driver.find_element_by_xpath("//*[@class='scoop-mtext' and text()='Masters']")
                self.submit1.click()
                time.sleep(5)

                # To check Depot Master in the application
                driver.find_element_by_link_text('Depot Master').click()
                time.sleep(4)
                driver.get_screenshot_as_file(path+"/"+"Depot_master" + timestamp + ".png")
                time.sleep(4)
                print("Validation of master tab is pass")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)