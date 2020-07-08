import allure
import pytest
from selenium import webdriver
import time
import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Test_Masters_Station_Type:

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

    def test_Station_Type(self, setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[5]/a").click()
        time.sleep(4)
        Station_Type_count = self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/div/div/mastertype/div[2]/div/div/extended-grid-cmp/div[2]/div/div[2]").text
        logging.info("Number of Station Types in VPSD app is : %s", Station_Type_count)
        count = 0
        Station_Type_count1 = 0
        for i in Station_Type_count:
            if count:
                Station_Type_count1 = i
            if i == ':':
                count = 1

        assert Station_Type_count1 == '2'

        logging.info("Station Type count is %s then Station Type count is as expected, Please continue",
                     Station_Type_count1)


    def test_Station_Type_Names(self,setup):

        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[5]/a").click()
        time.sleep(4)

        Station_Type_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[2]/div/div/span").text
        Station_Type_status = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[4]/div/span/span").text
        assert Station_Type_Name == "Terminal"
        assert Station_Type_status == 'Active'
        logging.info("Station Type Name 'Terminal' is present in the Application in active state and No spelling change")

        Station_Type_Name1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[2]/div/div/span").text
        Station_Type_status1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[4]/div/span/span").text
        assert Station_Type_Name1 == "Normal"
        assert Station_Type_status1 == 'Active'
        logging.info("Station Type Name 'Normal' is present in the Application in active state and No spelling change")