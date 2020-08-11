import unittest
from selenium import webdriver
import time

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://google.com")
        print(self.driver.title)
        self.driver.close()

    def test_VPSD_site(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://hublibrt.com:2001")
        time.sleep(30)
        print(self.driver.title)
        time.sleep(30)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()