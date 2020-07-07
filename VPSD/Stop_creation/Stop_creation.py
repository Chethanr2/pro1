import unittest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import pandas as pd
import datetime
import os
from selenium.webdriver.support.ui import Select

#timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#path = "G:/Chethan/Python notes/Selenium programs/VPSD/Stop_creation/Screenshots"+timestamp
#os.mkdir(path)

class VPSD_Stop_creation_Tab(unittest.TestCase):

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

                driver.find_element_by_xpath("//*[@class='btn btn-default btn-block blue_btn']").click()
                time.sleep(5)
                driver.find_element_by_xpath("//*[@class='btn btn-primary']").click()
                time.sleep(3)
                df = pd.read_excel('F:/Chethan/STUDY/Python notes/Selenium programs/VPSD/Stop_creation/Stops_Input.xlsx')
                Station_name = df['B'][0]
                driver.find_element_by_name('StationName').send_keys(Station_name)
                time.sleep(3)
                Station_short_name = df['B'][1]
                driver.find_element_by_xpath("//*[@name='StationShortName']").send_keys(Station_short_name)
                time.sleep(3)

                driver.find_element_by_name('DepotName').click()
                depot_value = df['B'][2]

                if depot_value == 'Hubli City Line':
                    sel = Select(driver.find_element_by_name('DepotName'))
                    sel.select_by_value('1: 37')
                    time.sleep(3)
                elif depot_value == 'Dharwad BRTS':
                    sel = Select(driver.find_element_by_name('DepotName'))
                    sel.select_by_value('2: 42')
                    time.sleep(3)
                elif depot_value == 'Dharwad City Line':
                    sel = Select(driver.find_element_by_name('DepotName'))
                    sel.select_by_value('3: 41')
                    time.sleep(3)
                elif depot_value == 'Hubli BRTS':
                    sel = Select(driver.find_element_by_name('DepotName'))
                    sel.select_by_value('4: 38')
                    time.sleep(3)
                else:
                    print ("Wrong input is selected")
                    exit(0)

                Station_location = df['B'][3]
                driver.find_element_by_name('StationArea').send_keys(Station_location)

                driver.find_element_by_name('StationType').click()
                depot_value = df['B'][4]

                if depot_value == 'Normal':
                    sel = Select(driver.find_element_by_name('StationType'))
                    sel.select_by_value('1: 6')
                    time.sleep(3)
                elif depot_value == 'Terminal':
                    sel = Select(driver.find_element_by_name('StationType'))
                    sel.select_by_value('2: 7')
                    time.sleep(3)
                else:
                    print("Wrong input is selected")
                    exit(0)

                driver.find_element_by_name('StationName').click()
                time.sleep(5)
                driver.find_element_by_xpath("//*[@class='btn btn-primary' and text() = 'Add Stops']").click()
                time.sleep(4)

                StopName = df['B'][5]
                driver.find_element_by_name('StopName').send_keys(StopName)
                time.sleep(3)

                driver.find_element_by_name('StopType').click()
                Stop_type = df['B'][6]

                if Stop_type == 'Normal':
                    sel = Select(driver.find_element_by_name('StopType'))
                    sel.select_by_value('1: 28')
                    time.sleep(3)
                elif Stop_type == 'Parking':
                    sel = Select(driver.find_element_by_name('StopType'))
                    sel.select_by_value('2: 29')
                    time.sleep(3)
                else:
                    print("Wrong input is selected")
                    exit(0)

                driver.find_element_by_name('Services').click()
                service_Type = df['B'][7]
                driver.find_element_by_link_text(service_Type).click()
                #driver.find_element_by_xpath("//*[@class='dropdown-item' and text() = 'City']").click()
                #driver.find_element_by_id("//*[@id='tab-1']/div[2]/form/div[2]/div[4]/div/ss-multiselect-dropdown/div/ul/li[4]/a").click()
                #driver.find_element_by_xpath("//*[contains(text(), 'City')]").click()//*[@id="tab-1"]/div[2]/form/div[2]/div[4]/div/ss-multiselect-dropdown/div/ul/li[4]/a


                driver.find_element_by_xpath("//*[@class='checked_text bold_text']").click()
                time.sleep(3)
                Stop_lat = str(df['B'][8])
                driver.find_element_by_name('StopLatitude').send_keys(Stop_lat)
                time.sleep(3)

                Stop_long = str(df['B'][9])
                driver.find_element_by_name('StopLongitude').send_keys(Stop_long)
                time.sleep(3)

                driver.find_element_by_name('Facilities').click()
                driver.find_element_by_link_text("Drinking Water").click()
                driver.find_element_by_link_text("Wifi").click()
                time.sleep(4)


            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)