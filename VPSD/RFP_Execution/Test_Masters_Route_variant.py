import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Test_Masters_Route_Variant:

    @pytest.fixture()
    def setup(self):
        ''' Setup for the entire module '''
        logging.info('Inside the setup module')
        self.driver = webdriver.Chrome()
        self.driver.get("http://nechubli.com:5001/")
        self.driver.implicitly_wait(40)
        UserName = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME, 'userID')))
        self.driver.maximize_window()

        #UserName = self.driver.find_element_by_name('userID')
        UserName.clear()
        UserName.send_keys('VPSD')
        Password = self.driver.find_element_by_name('password')
        Password.clear()
        Password.send_keys('Vpsd@master@123')
        time.sleep(4)

        self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div/div/div/div/div[2]/div[2]/div/form[1]/div/div[3]/div[1]/button").click()
        time.sleep(20)

        yield
        self.driver.close()

    def test_login(self, setup):
        try:
            assert self.driver.title == 'VPSD System'
            logging.info("Hitting the correct URL Please proceed for further execution")
            time.sleep(2)

        except:
            logging.info("Hitting the wrong URL please check and try again")

    def test_Route_variant_Count(self, setup):

        self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[7]/a").click()
        time.sleep(4)
        Route_variant_count = self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div[2]/div/div/div/mastertype/div[2]/div/div/extended-grid-cmp/div[2]/div/div[2]").text
        logging.info("Number of route Variant in VPSD app is : %s", Route_variant_count)
        count = 0
        Route_variant_count1 = 0
        for i in Route_variant_count:
            if count:
                Route_variant_count1 = i
            if i == ':':
                count = 1

        assert Route_variant_count1 == '3'

        logging.info("Route Variant count is %s then Route variant count is as expected, Please continue",
                     Route_variant_count1)


    def test_Route_variant_Names(self,setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[7]/a").click()
        time.sleep(4)

        Route_Variant_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[2]/div/div/span").text
        Route_variant_Name_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[4]/div/span/span").text
        assert Route_Variant_Name == "General"
        assert Route_variant_Name_status == 'Active'
        logging.info("Route Variant Name 'General' is present in the Application in active state and No spelling change")

        Route_Variant_Name1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[2]/div/div/span").text
        Route_variant_Name1_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[4]/div/span/span").text
        assert Route_Variant_Name1 == "Ladies"
        assert Route_variant_Name1_status == 'Active'
        logging.info("ROute Variant Name 'Ladies' is present in the application in active state and No spelling change")

        Route_Variant_Name2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[2]/div/div/span").text
        Route_variant_Name2_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[4]/div/span/span").text
        assert Route_Variant_Name2 == "Normal"
        assert Route_variant_Name2_status == 'Active'
        logging.info("Route Variant Name 'Normal' is present in the application in active state and No spelling change")