import allure
import pytest
from selenium import webdriver
import time
import logging

# logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Test_Masters_Depot:

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

    def test_Masters_Dharwad_BRT_Depot(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[8]/a").click()
        time.sleep(4)

        Dharwad_BRT_depot_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[1]/div/div/span").text
        assert Dharwad_BRT_depot_Code == 'DEP000009'
        logging.info("Dharwad BRT Depot code is : %s ",Dharwad_BRT_depot_Code)

        Dharwad_BRT_Depot_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[2]/div/div/span").text
        assert Dharwad_BRT_Depot_Name == 'Dharwad BRTS'
        logging.info("Dharwad BRT Depot Name is : %s",Dharwad_BRT_Depot_Name)

        Dharwad_BRT_Division_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[3]/div/div/span").text
        assert Dharwad_BRT_Division_Code == 'D2'
        logging.info("Dharwad BRT Divison Code is : %s",Dharwad_BRT_Division_Code)

        Dharwad_BRT_Lat = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[6]/div/div/span").text
        Dharwad_BRT_Long = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[1]/td[7]/div/div/span").text
        assert Dharwad_BRT_Lat == '15.471000'
        assert Dharwad_BRT_Long == '74.993462'
        logging.info("Dharwad BRT Latitude and Longitude is : %s & %s",Dharwad_BRT_Lat,Dharwad_BRT_Long)

    def test_Masters_Dharwad_City_Depot(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[8]/a").click()
        time.sleep(4)

        Dharwad_City_depot_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[1]/div/div/span").text
        assert Dharwad_City_depot_Code == 'DEP000008'
        logging.info("Dharwad City Depot code is : %s ",Dharwad_City_depot_Code)

        Dharwad_City_Depot_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[2]/div/div/span").text
        assert Dharwad_City_Depot_Name == 'Dharwad City Line'
        logging.info("Dharwad City Depot Name is : %s",Dharwad_City_Depot_Name)


        Dharwad_City_Division_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[3]/div/div/span").text
        assert Dharwad_City_Division_Code == 'D2'
        logging.info("Dharwad City Divison Code is : %s",Dharwad_City_Division_Code)

        Dharwad_City_Lat = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[6]/div/div/span").text
        Dharwad_City_Long = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[7]/div/div/span").text
        assert Dharwad_City_Lat == '15.466754'
        assert Dharwad_City_Long == '75.017222'
        logging.info("Dharwad City Latitude and Longitude is : %s & %s",Dharwad_City_Lat,Dharwad_City_Long)

    def test_Masters_Hubli_City_Depot(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[8]/a").click()
        time.sleep(4)

        Hubli_City_depot_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[1]/div/div/span").text
        assert Hubli_City_depot_Code == 'DEP000004'
        logging.info("Hubli City Depot code is : %s ",Hubli_City_depot_Code)

        Hubli_City_Depot_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[2]/div/div/span").text
        assert Hubli_City_Depot_Name == 'Hubli City Line'
        logging.info("Hubli City Depot Name is : %s",Hubli_City_Depot_Name)

        Hubli_City_Division_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[3]/div/div/span").text
        assert Hubli_City_Division_Code == 'D1'
        logging.info("Hubli City Division Code is : %s",Hubli_City_Division_Code)

        Hubli_City_Lat = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[6]/div/div/span").text
        Hubli_City_Long = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[7]/div/div/span").text
        assert Hubli_City_Lat == '15.356047'
        assert Hubli_City_Long == '75.128968'
        logging.info("Hubli City Latitude and Longitude is : %s & %s",Hubli_City_Lat,Hubli_City_Long)

    def test_Masters_Hubli_BRT_Depot(self, setup):
        self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/a/span[2]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[5]/div/div/div[2]/ul/li[8]/a").click()
        time.sleep(4)

        Hubli_BRT_depot_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[1]/div/div/span").text
        assert Hubli_BRT_depot_Code == 'DEP000033'
        logging.info("Hubli BRT Depot code is : %s ", Hubli_BRT_depot_Code)

        Hubli_BRT_Depot_Name = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[2]/div/div/span").text
        assert Hubli_BRT_Depot_Name == 'Hubli BRTS'
        logging.info("Hubli BRT Depot Name is : %s", Hubli_BRT_Depot_Name)

        Hubli_BRT_Division_Code = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[3]/div/div/span").text
        assert Hubli_BRT_Division_Code == 'D1'
        logging.info("Hubli BRT Divison Code is : %s", Hubli_BRT_Division_Code)

        Hubli_BRT_Lat = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[6]/div/div/span").text
        Hubli_BRT_Long = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[7]/div/div/span").text
        assert Hubli_BRT_Lat == '15.349241'
        assert Hubli_BRT_Long == '75.118043'
        logging.info("Hubli BRT Latitude and Longitude is : %s & %s", Hubli_BRT_Lat, Hubli_BRT_Long)



