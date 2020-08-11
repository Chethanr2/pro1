import allure
import pytest
from selenium import webdriver
import time
import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

Service_count1 = 0
class Test_Masters_Service_Type:

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

    def test_Service_Type(self, setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[3]/a").click()
        time.sleep(4)
        Service_Type_count = self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/mastertype/div[2]/div/div/extended-grid-cmp/div[2]/div/div[2]").text
        logging.info("Number of Service Types in VPSD app is : %s", Service_Type_count)
        count = 0
        global Service_count1
        for i in Service_Type_count:
            if count:
                Service_count1 = i
            if i == ':':
                count = 1

        assert Service_count1 == '6'

        logging.info("Service Type count is %s then Service Type count is as expected, Please continue",
                     Service_count1)


    def test_Service_Type_Names(self,setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[3]/a").click()
        time.sleep(4)

        Service_Type_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[2]/div/div/span").text
        Service_Type_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[6]/div/span/span").text
        assert Service_Type_Name == "City"
        assert Service_Type_status == 'Active'
        logging.info("Service Type Name 'City' is present in the Application in active state and No spelling change")

        Service_Type_Name1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[2]/div/div/span").text
        Service_Type_status1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[6]/div/span/span").text
        assert Service_Type_Name1 == "All Stops"
        assert Service_Type_status1 == 'Active'
        logging.info("Station Type Name 'All Stops' is present in the Application in active state and No spelling change")

        Service_Type_Name2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[2]/div/div/span").text
        Service_Type_status2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[6]/div/span/span").text
        assert Service_Type_Name2 == "Limited Stops"
        assert Service_Type_status2 == 'Active'
        logging.info("Station Type Name 'Limited Stops' is present in the Application in active state and No spelling change")

        Service_Type_Name3 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[2]/div/div/span").text
        Service_Type_status3 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[6]/div/span/span").text
        assert Service_Type_Name3 == "Feeder"
        assert Service_Type_status3 == 'Active'
        logging.info("Station Type Name 'Feeder' is present in the Application in active state and No spelling change")

        Service_Type_Name4 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[5]/td[2]/div/div/span").text
        Service_Type_status4 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[5]/td[6]/div/span/span").text
        assert Service_Type_Name4 == "Suburban"
        assert Service_Type_status4 == 'Active'
        logging.info("Station Type Name 'Suburban' is present in the Application in active state and No spelling change")

        Service_Type_Name5 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[6]/td[2]/div/div/span").text
        Service_Type_status5 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[6]/td[6]/div/span/span").text
        assert Service_Type_Name5 == "Express"
        assert Service_Type_status5 == 'Active'
        logging.info("Station Type Name 'Express' is present in the Application in active state and No spelling change")