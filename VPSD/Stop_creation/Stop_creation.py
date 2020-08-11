import pytest
from urllib.request import urlopen
from selenium import webdriver
import time
import requests
import pandas as pd
from selenium.webdriver.support.ui import Select

#timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#path = "G:/Chethan/Python notes/Selenium programs/VPSD/Stop_creation/Screenshots"+timestamp
#os.mkdir(path)

class Test_Stop_creation_Tab:

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
            time.sleep(20)

            yield
            driver.close()

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_Stop_creation_VPSD(self,setup):
        driver = self.driver
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
            print("Wrong input is selected")
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

        driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[2]/div[4]/div/ss-multiselect-dropdown/div").click()
        service_Type = df['B'][7]
        li = list(service_Type.split(","))
        print("Number of service type involved : %s" , li)
        Count_length_service_type = len(li)
        count = 0
        while Count_length_service_type:
            driver.find_element_by_link_text(li[count]).click()
            Count_length_service_type = Count_length_service_type - 1
            count = count + 1
            time.sleep(4)

        # driver.find_element_by_xpath("//*[@class='dropdown-item' and text() = 'City']").click()
        # driver.find_element_by_id("//*[@id='tab-1']/div[2]/form/div[2]/div[4]/div/ss-multiselect-dropdown/div/ul/li[4]/a").click()
        # driver.find_element_by_xpath("//*[contains(text(), 'City')]").click()//*[@id="tab-1"]/div[2]/form/div[2]/div[4]/div/ss-multiselect-dropdown/div/ul/li[4]/a

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

        #driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[4]/div[5]/div/button[1]").click()
        #time.sleep(3)
        obj = driver.find_element_by_name('StopColorId')
        obj.click()
        all_options = obj.find_elements_by_tag_name("option")


        Color_code = df['B'][10]
        for options in all_options:
            print("Options in all options are : ", options.text.strip())

        for options in all_options:
            if options.text.strip() == Color_code :
                options.click()
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='tab-1']/div[2]/form/div[4]/div[5]/div").click()
                time.sleep(3)

        time.sleep(6)