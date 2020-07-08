import allure
import pytest
from selenium import webdriver
import time
import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Test_Masters_Route_Catogery:

    @pytest.fixture()
    def setup(self):
        ''' Setup for the entire module '''
        logging.info('Inside the setup module')
        self.driver = webdriver.Chrome()
        self.driver.get("http://nechubli.com:5001/")
        self.driver.implicitly_wait(40)
        self.driver.maximize_window()

        UserName = self.driver.find_element_by_name('userID')
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

    def test_Route_Catogery_Count(self, setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[6]/a").click()
        time.sleep(4)
        Route_catogery_count = self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/mastertype/div[2]/div/div/extended-grid-cmp/div[2]/div/div[2]").text
        logging.info("Number of Route Catogery in VPSD app is : %s", Route_catogery_count)
        count = 0
        Route_catogery_count1 = 0
        for i in Route_catogery_count:
            if count:
                Route_catogery_count1 = i
            if i == ':':
                count = 1

        assert Route_catogery_count1 == '3'

        logging.info("Route Catogery count is %s then Route Catogery count is as expected, Please continue",
                     Route_catogery_count1)


    def test_Route_catogery_Names(self,setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[6]/a").click()
        time.sleep(4)

        Route_Catogery_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[2]/div/div/span").text
        Route_Catogery_Name_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[4]/div/span/span").text
        assert Route_Catogery_Name == "Chartered"
        assert Route_Catogery_Name_status == 'Active'
        logging.info("Route Catogery Name 'Chartered' is present in the Application in active state and No spelling change")

        Route_Catogery_Name1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[2]/div/div/span").text
        Route_Catogery_Name1_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[4]/div/span/span").text
        assert Route_Catogery_Name1 == "Revenue"
        assert Route_Catogery_Name1_status == 'Active'
        logging.info("Route Catogery Name 'Revenue' is present in the application in active state and No spelling change")

        Route_Catogery_Name2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[2]/div/div/span").text
        Route_Catogery_Name2_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[4]/div/span/span").text
        assert Route_Catogery_Name2 == "Dead"
        assert Route_Catogery_Name2_status == 'Active'
        logging.info("Route Catogery Name 'Dead' is present in the application in active state and No spelling change")