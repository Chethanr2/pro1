import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/Route_tab"+timestamp
os.mkdir(path)

class VPSD_cRoute_Tab(unittest.TestCase):

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
                self.password.send_keys("Vpsd@master@123")
                self.submit.click()
                self.assertIn("Vehicle Planning and Scheduling System", driver.page_source)
                time.sleep(20)
                print("Validating the Route tab")
                self.submit1 = driver.find_element_by_xpath("//*[@class='scoop-mtext' and text()='Route']").click()
                time.sleep(5)

                print("Validation of Route category")
                obj = driver.find_element_by_name('RouteCategoryId')
                all_options = obj.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        print("pass")
                        option.click()
                    elif option.text.strip() == 'Chartered':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Route_chartered"+timestamp+".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Dead':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Route_dead"+timestamp+".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Revenue':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Route_revenue"+timestamp+".png")
                        time.sleep(4)
                    else:
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Route category validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(10)

                print("Validation of Route Variant")
                obj1 = driver.find_element_by_name('RouteVariantId')
                all_options = obj1.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                    elif option.text.strip() == 'Normal':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Route_normal"+timestamp+".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Ladies':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Route_ladies"+timestamp+".png")
                        time.sleep(4)
                    else:
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Route Variant validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(10)

                print("Validation of Line type")
                obj2 = driver.find_element_by_name('LineTypeId')
                all_options = obj2.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                        time.sleep(4)
                    elif option.text.strip() == 'Hubli Division':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Line_type_hubli"+timestamp+".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Dharwad Division':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        driver.get_screenshot_as_file(path+"/"+"Line_type_dharwad"+timestamp+".png")
                        time.sleep(4)
                    else:
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Line type validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(10)

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)