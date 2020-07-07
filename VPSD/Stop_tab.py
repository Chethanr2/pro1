import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import datetime
import os

#timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#path = "G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/Stop_tab"+timestamp
#os.mkdir(path)

class VPSD_bStop_Tab(unittest.TestCase):

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
                time.sleep(10)
                #driver.get_screenshot_as_file(path +"/"+ "VPSD_login_page" + timestamp + ".png")
                time.sleep(5)
                print ("Testing Stop tab")
                self.submit1 = driver.find_element_by_xpath("//*[@class='btn btn-default btn-block blue_btn']")
                self.submit1.click()
                time.sleep(5)

                obj = driver.find_element_by_xpath("(//*[@name='ServiceType'])[3]")
                obj.click()
                all_options = obj.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        print("pass")
                        option.click()
                    elif option.text.strip() == 'City':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "service_type_city" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'BRT':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Service_type_BRT" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Express BRT':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Service_type_ExpressBRT" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Suburban':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Service_type_suburban" + timestamp + ".png")
                        time.sleep(4)
                    else :
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Service type validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(5)

                print("Validating the station type")
                obj = driver.find_element_by_name('StationType')
                all_options = obj.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        print("pass")
                        option.click()
                    elif option.text.strip() == 'Normal':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stations_normal" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Terminal':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stations_terminal" + timestamp + ".png")
                        time.sleep(4)
                    else :
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Station type validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(10)

                print("Validating the stop type")
                obj1 = driver.find_element_by_name('StopType')
                all_options = obj1.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stations_terminal" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Normal':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stations_terminal" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Parking':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path +"/"+ "Stations_terminal" + timestamp + ".png")
                        time.sleep(4)
                    else:
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Stop type validation is pass")
                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                time.sleep(10)
                
                print("Validating the Depot Names")
                obj2 = driver.find_element_by_name('DepotName')
                all_options = obj2.find_elements_by_tag_name("option")

                for option in all_options:
                    if option.text.strip() == '--Select--':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Total_stops" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Hubli City Line':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stops_Hubli_city_line" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Hubli BRTS':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stops_Hubli_brts" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Dharwad BRTS':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stops_Dharwad_brts" + timestamp + ".png")
                        time.sleep(4)
                    elif option.text.strip() == 'Dharwad City Line':
                        option.click()
                        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
                        time.sleep(4)
                        #driver.get_screenshot_as_file(path+"/" + "Stops_Dharwad_city_line" + timestamp + ".png")
                        time.sleep(4)
                    else:
                        print("wrong option in build")
                        break
                    time.sleep(2)

                print("Depot Name validation is pass")
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