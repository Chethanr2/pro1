import pytest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import pandas as pd
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
from selenium.webdriver.support.ui import Select


class Test_Stop_edit_Tab:

    @pytest.fixture()
    def setup(self):
        try:
            stri = "http://nechubli.com:5001"
            df = pd.read_excel('F:/Chethan/STUDY/Python notes/Selenium programs/VPSD/Stop_creation/Stops_Input.xlsx')
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            URL = df['D'][0]
            self.driver.get(URL)
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)

            driver = self.driver

            assert "VPSD System" == driver.title
            UserName = df['D'][1]
            self.User_name = driver.find_element_by_id('UserName')
           # self.User_name.send_keys(UserName)
            Pass_word = df['D'][2]
            self.password = driver.find_element_by_id('Password')
            #self.password.send_keys(Pass_word)
            self.submit = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()
            self.User_name.send_keys(UserName)
            self.password.send_keys(Pass_word)
            self.submit.click()
            #assert "Vehicle Planning and Scheduling System" == driver.page_source
            time.sleep(40)

            yield
            driver.close()

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_Stop_edit_VPSD(self,setup):
        driver = self.driver
        driver.find_element_by_xpath("//*[@class='btn btn-default btn-block blue_btn']").click() # Click on stop menu
        time.sleep(3)
        df = pd.read_excel('F:/Chethan/STUDY/Python notes/Selenium programs/VPSD/Stop_creation/Stops_Input.xlsx')
        Station_name = df['B'][12]
        driver.find_element_by_xpath("//*[@id='country']").send_keys(Station_name)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/stopmst-com/div[1]/div/div[1]/div[2]/div[7]/div/button").click() #Click on search button
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr/td[8]/div/span/span/span[1]/hasactionpermission").click()
        time.sleep(3)

        Is_station_code_editable = driver.find_element_by_xpath("//*[@id='stpid']").is_enabled()
        if Is_station_code_editable == True:
            logging.info("Station Code is editable, this is wrong ")
            assert Is_station_code_editable == True
        elif Is_station_code_editable == False:
            logging.info("Station code is not editable which is correct please proceed")
        time.sleep(3)

        Station_name_editable = driver.find_element_by_xpath("//*[@id='station']/form/div[2]/div[2]/div/input").is_enabled()
        if Station_name_editable == True:
            logging.info("Station name is editable, This is correct")
        elif Station_name_editable == False:
            logging.info("Station Name is not editable, This is wrong")
        time.sleep(3)

        Is_station_short_name = driver.find_element_by_xpath("//*[@id='stationShortName']").click()
        if Is_station_short_name == True:
            logging.info("Station short name is editable, This is wrong")
        elif Is_station_short_name == False:
            logging.info("Station short name is not editable, This is correct")
        time.sleep(3)

        Depot_Name_editable = driver.find_element_by_xpath("//*[@id='station']/form/div[2]/div[4]/div/select").is_enabled()
        if Depot_Name_editable == True:
            logging.info("Depot Name is editable,This is correct, Please proceed")
        elif Depot_Name_editable == False:
            logging.info("Depot name is not editable, This is wrong")
        time.sleep(3)

        Station_area_editable = driver.find_element_by_xpath("//*[@id='StationArea']").is_enabled()
        if Station_area_editable == True:
            logging.info("Station area is editable, This is wrong")
        elif Station_area_editable == False:
            logging.info("Station area is not editable, This is correct")
        time.sleep(3)

        Station_type_editable = driver.find_element_by_xpath("//*[@id='station']/form/div[3]/div[2]/div/select").is_enabled()
        if Station_type_editable == True:
            logging.info("Station type is editable, This is wrong")
        elif Station_type_editable == False:
            logging.info("Station type is not editable, This is correct")
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='station']/form/div[3]/div[4]/div/button[1]").click()
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[9]/div/span/span/span/hasactionpermission").click()
        time.sleep(3)

        Is_Stop_number_editable = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[2]/div[1]/div/input").is_enabled()
        if Is_Stop_number_editable == True:
            logging.info("Stop number is editable, This is wrong")
        elif Is_Stop_number_editable == False:
            logging.info("Stop number is not editable, This is correct")
        time.sleep(3)

        # Stop name is enabled only when stop is not used in any route or route is in inactive state

        Is_Stop_Name_Editable = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[2]/div[2]/div/input").is_enabled()
        if Is_Stop_Name_Editable == True:
            logging.info("Stop name is editable, This is wrong")
        elif Is_Stop_Name_Editable == False:
            logging.info("Stop name is not editable, This is correct")
        time.sleep(3)

        Is_Stop_type_editable = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[2]/div[3]/div/select").is_enabled()
        if Is_Stop_type_editable == True:
            logging.info("Stop type is editable, This is wrong")
        elif Is_Stop_type_editable == False:
            logging.info("Stop type is not editable, This is correct")
        time.sleep(3)

        # Latitude and longitude is enabled only when stop is not used in any route or route is in inactive state
        Is_Latitude_editable = driver.find_element_by_xpath("//*[@id='stpLat']").is_enabled()
        if Is_Latitude_editable == True:
            logging.info("Stop latitude is editable, This is wrong")
        elif Is_Latitude_editable == False:
            logging.info("Stop Latitude is not editable, This is correct")
        time.sleep(3)

        Is_Longitude_editable = driver.find_element_by_xpath("//*[@id='stpLng']").is_enabled()
        if Is_Longitude_editable == True:
            logging.info("Stop longitude is editable, This is wrong")
        elif Is_Longitude_editable == False:
            logging.info("Stop longitude is not editable, This is correct")
        time.sleep(3)

        Is_Bunching_enabled = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[3]/div[4]/div/select").is_enabled()
        if Is_Bunching_enabled == True:
            logging.info("Bunching is editable, This is correct please proceed")
        elif Is_Bunching_enabled == False:
            logging.info("Bunching is not editable, This is wrong")
        time.sleep(3)

        Is_Opposite_enabled = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[4]/div[1]/div/select").is_enabled()
        if Is_Opposite_enabled == True:
            logging.info("Opposite stop is editable, This is correct please proceed")
        elif Is_Opposite_enabled == False:
            logging.info("Opposite stop is not editable, This is wrong")
        time.sleep(3)

        Is_Facilities_enabled = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[4]/div[2]/div/ss-multiselect-dropdown/div/button").is_enabled()
        if Is_Facilities_enabled == True:
            logging.info("Facilities Available is editable, This is correct please proceed")
        elif Is_Facilities_enabled == False:
            logging.info("Facilities Available is not editable, This is wrong")
        time.sleep(3)

        Is_Color_code_Enabled = driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[4]/div[4]/div/select").is_enabled()
        if Is_Color_code_Enabled == True:
            logging.info("Color Code is editable, This is correct please proceed")
        elif Is_Color_code_Enabled == False:
            logging.info("Color Code is not editable, This is wrong")

        time.sleep(6)