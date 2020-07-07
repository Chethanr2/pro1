import allure
import pytest
from selenium import webdriver
import time
import logging
#logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Test_Business_rules:

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

        self.driver.find_element_by_xpath("//*[@id='scoop']/div/div/div/div/div[2]/div[2]/div/form[1]/div/div[3]/div[1]/button").click()
        time.sleep(20)

        yield
        self.driver.close()

    def test_login(self, setup):
        try:
            assert self.driver.title == 'VPSD System'
            logging.info("Hitting the correct URL Please proceed for further execution")
            time.sleep(2)

        except :
            logging.info("Hitting the wrong URL please check and try again")

    
    def test_Business_rule_1(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)
        Busi1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[3]/div/div/span").text

        vaule_Business_rule1 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[6]/div/div/span").text

        assert vaule_Business_rule1 == 'Yes'
        logging.info("%s is set to : %s", Busi1,vaule_Business_rule1)
        time.sleep(3)

        Busi1_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[2]/td[8]/div/span/span").text
        assert Busi1_active == 'Active'
        logging.info("Status of the business rule : %s",Busi1_active)
        time.sleep(3)

    def test_business_rule_2(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[3]/div/div/span").text

        value_business_rule2 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[6]/div/div/span").text
        assert value_business_rule2 == '240'
        logging.info("%s is set to : %s",Busi2,value_business_rule2)
        time.sleep(3)

        Busi2_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[3]/td[8]/div/span/span").text
        assert Busi2_active == 'Active'
        logging.info("Status of the business rule : %s", Busi2_active)
        time.sleep(3)

    def test_business_rule_3(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi3 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[3]/div/div/span").text

        value_business_rule3 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[6]/div/div/span").text
        assert value_business_rule3 == '180'
        logging.info("%s is set to : %s",Busi3,value_business_rule3)
        time.sleep(4)

        Busi3_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[4]/td[8]/div/span/span").text
        assert Busi3_active == 'Active'
        logging.info("Status of the business rule : %s", Busi3_active)
        time.sleep(3)

    def test_business_rule_4(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi4 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[5]/td[3]/div/div/span").text

        value_business_rule4 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[5]/td[6]/div/div/span").text
        assert value_business_rule4 == '10'
        logging.info("%s is set to : %s", Busi4, value_business_rule4)
        time.sleep(4)

        Busi4_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[5]/td[8]/div/span/span").text
        assert Busi4_active == 'Active'
        logging.info("Status of the business rule : %s", Busi4_active)
        time.sleep(3)

    def test_business_rule_5(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi5 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[6]/td[3]/div/div/span").text

        value_business_rule5 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[6]/td[6]/div/div/span").text
        assert value_business_rule5 == '15'
        logging.info("%s is set to : %s", Busi5, value_business_rule5)
        time.sleep(4)

        Busi5_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[6]/td[8]/div/span/span").text
        assert Busi5_active == 'Active'
        logging.info("Status of the business rule : %s", Busi5_active)
        time.sleep(3)

    def test_business_rule_6(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi6 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[7]/td[3]/div/div/span").text

        value_business_rule6 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[7]/td[6]/div/div/span").text
        assert value_business_rule6 == '25'
        logging.info("%s is set to : %s", Busi6, value_business_rule6)
        time.sleep(4)

        Busi6_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[7]/td[8]/div/span/span").text
        assert Busi6_active == 'Active'
        logging.info("Status of the business rule : %s", Busi6_active)
        time.sleep(3)

    def test_business_rule_7(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi7 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[8]/td[3]/div/div/span").text

        value_business_rule7 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[8]/td[6]/div/div/span").text
        assert value_business_rule7 == 'Yes'
        logging.info("%s is set to : %s", Busi7, value_business_rule7)
        time.sleep(4)

        Busi7_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[8]/td[8]/div/span/span").text
        assert Busi7_active == 'Active'
        logging.info("Status of the business rule : %s", Busi7_active)
        time.sleep(3)

    def test_business_rule_8(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi8 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[9]/td[3]/div/div/span").text

        value_business_rule8 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[9]/td[6]/div/div/span").text
        assert value_business_rule8 == 'No'
        logging.info("%s is set to : %s", Busi8, value_business_rule8)
        time.sleep(4)

        Busi8_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[9]/td[8]/div/span/span").text
        assert Busi8_active == 'Active'
        logging.info("Status of the business rule : %s", Busi8_active)
        time.sleep(3)
        

    def test_business_rule_9(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi9 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[10]/td[3]/div/div/span").text

        value_business_rule9 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[10]/td[6]/div/div/span").text
        assert value_business_rule9 == 'No'
        logging.info("%s is set to : %s", Busi9, value_business_rule9)
        time.sleep(4)

        Busi9_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[10]/td[8]/div/span/span").text
        assert Busi9_active == 'Active'
        logging.info("Status of the business rule : %s", Busi9_active)
        time.sleep(3)
    
    def test_business_rule_10(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi10 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[11]/td[3]/div/div/span").text

        value_business_rule10 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[11]/td[6]/div/div/span").text
        assert value_business_rule10 == 'No'
        logging.info("%s is set to : %s", Busi10, value_business_rule10)
        time.sleep(4)

        Busi10_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[11]/td[8]/div/span/span").text
        assert Busi10_active == 'Active'
        logging.info("Status of the business rule : %s", Busi10_active)
        time.sleep(3)
        
    def test_business_rule_11(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi11 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[12]/td[3]/div/div/span").text

        value1_business_rule11 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[12]/td[6]/div/div/span").text
        value2_business_rule11 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[12]/td[7]/div/div/span").text
        assert value1_business_rule11 == '18:00'
        assert value2_business_rule11 == '18:10'
        logging.info("%s is set between : %s to %s", Busi11, value1_business_rule11,value2_business_rule11)
        time.sleep(4)

        Busi11_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[12]/td[8]/div/span/span").text
        assert Busi11_active == 'Active'
        logging.info("Status of the business rule : %s", Busi11_active)
        time.sleep(3)


    def test_business_rule_12(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi12 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[13]/td[3]/div/div/span").text

        value1_business_rule12 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[13]/td[6]/div/div/span").text
        
        assert value1_business_rule12 == 'No'
        
        logging.info("%s is set : %s", Busi12, value1_business_rule12)
        time.sleep(4)
        
        Busi12_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[13]/td[8]/div/span/span").text
        assert Busi12_active == 'Active'
        logging.info("Status of the business rule : %s", Busi12_active)
        time.sleep(3)

    def test_business_rule_13(self, setup):
        self.driver.find_element_by_xpath(
            "//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi13 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[14]/td[3]/div/div/span").text

        value1_business_rule13 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[14]/td[6]/div/div/span").text

        assert value1_business_rule13 == '720'

        logging.info("%s is set : %s", Busi13, value1_business_rule13)
        time.sleep(4)

        Busi13_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[14]/td[8]/div/span/span").text
        assert Busi13_active == 'Active'
        logging.info("Status of the business rule : %s", Busi13_active)
        time.sleep(3)

    def test_business_rule_14(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi14 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[15]/td[3]/div/div/span").text

        value1_business_rule14 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[15]/td[6]/div/div/span").text

        assert value1_business_rule14 == '480'

        logging.info("%s is set : %s", Busi14, value1_business_rule14)
        time.sleep(4)

        Busi14_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[15]/td[8]/div/span/span").text
        assert Busi14_active == 'Active'
        logging.info("Status of the business rule : %s", Busi14_active)
        time.sleep(3)

    def test_business_rule_15(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi15 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[16]/td[3]/div/div/span").text

        value1_business_rule15 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[16]/td[6]/div/div/span").text
        value2_business_rule15 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[16]/td[7]/div/div/span").text

        assert value1_business_rule15 == '08:30'
        assert value2_business_rule15 == '08:40'

        logging.info("%s is set between : %s to %s", Busi15, value1_business_rule15,value2_business_rule15)
        time.sleep(4)

        Busi15_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[16]/td[8]/div/span/span").text
        assert Busi15_active == 'Active'
        logging.info("Status of the business rule : %s", Busi15_active)
        time.sleep(3)


    def test_business_rule_16(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi16 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[17]/td[3]/div/div/span").text

        value1_business_rule16 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[17]/td[6]/div/div/span").text

        assert value1_business_rule16 == '15'

        logging.info("%s is set : %s", Busi16, value1_business_rule16)
        time.sleep(4)

        Busi16_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[17]/td[8]/div/span/span").text
        assert Busi16_active == 'Active'
        logging.info("Status of the business rule : %s", Busi16_active)
        time.sleep(3)

    def test_business_rule_17(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi17 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[18]/td[3]/div/div/span").text

        value1_business_rule17 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[18]/td[6]/div/div/span").text

        assert value1_business_rule17 == '15'

        logging.info("%s is set : %s", Busi17, value1_business_rule17)
        time.sleep(4)

        Busi17_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[18]/td[8]/div/span/span").text
        assert Busi17_active == 'Active'
        logging.info("Status of the business rule : %s", Busi17_active)
        time.sleep(3)
        

    def test_business_rule_18(self,setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi18 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[19]/td[3]/div/div/span").text

        value1_business_rule18 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[19]/td[6]/div/div/span").text

        assert value1_business_rule18 == '180'

        logging.info("%s is set : %s", Busi18, value1_business_rule18)
        time.sleep(4)

        Busi18_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[19]/td[8]/div/span/span").text
        assert Busi18_active == 'Active'
        logging.info("Status of the business rule : %s", Busi18_active)
        time.sleep(3)

    def test_business_rule_19(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi19 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[20]/td[3]/div/div/span").text

        value1_business_rule19 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[20]/td[6]/div/div/span").text

        assert value1_business_rule19 == '60'

        logging.info("%s is set : %s", Busi19, value1_business_rule19)
        time.sleep(4)

        Busi19_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[20]/td[8]/div/span/span").text
        assert Busi19_active == 'Active'
        logging.info("Status of the business rule : %s", Busi19_active)
        time.sleep(3)

    def test_business_rule_20(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi20 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[21]/td[3]/div/div/span").text

        value1_business_rule20 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[21]/td[6]/div/div/span").text

        assert value1_business_rule20 == '40'

        logging.info("%s is set : %s", Busi20, value1_business_rule20)
        time.sleep(4)

        Busi20_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[21]/td[8]/div/span/span").text
        assert Busi20_active == 'Active'
        logging.info("Status of the business rule : %s", Busi20_active)
        time.sleep(3)

    def test_business_rule_21(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi21 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[22]/td[3]/div/div/span").text

        value1_business_rule21 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[22]/td[6]/div/div/span").text

        assert value1_business_rule21 == '10'

        logging.info("%s is set : %s", Busi21, value1_business_rule21)
        time.sleep(4)

        Busi21_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[22]/td[8]/div/span/span").text
        assert Busi21_active == 'Active'
        logging.info("Status of the business rule : %s", Busi21_active)
        time.sleep(3)

    def test_business_rule_22(self, setup):
        self.driver.find_element_by_xpath("//*[@id='scoop']/div[2]/div/sidemenu-cmp/nav/div/div/ul/li[8]/a/span[2]").click()
        time.sleep(3)

        Busi22 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[23]/td[3]/div/div/span").text

        value1_business_rule22 = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[23]/td[6]/div/div/span").text

        assert value1_business_rule22 == '07:00'

        logging.info("%s is set : %s", Busi22, value1_business_rule22)
        time.sleep(4)

        Busi22_active = self.driver.find_element_by_xpath("//*[@id='basic-table']/tbody/tr[23]/td[8]/div/span/span").text
        assert Busi22_active == 'Active'
        logging.info("Status of the business rule : %s", Busi22_active)
        time.sleep(3)