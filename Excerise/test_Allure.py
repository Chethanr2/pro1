import allure
import pytest
from selenium import webdriver
import time


class Test_Allure:

    def test_login(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://hublibrt.com:2001")
        time.sleep(30)
        title = self.driver.title

        if title == 'VPSD System':
            assert True
            self.driver.close()
        else:
            assert False
            self.driver.close()


    def test_employee(self):
        pytest.skip("As for now it will be skipped")
