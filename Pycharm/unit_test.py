from selenium import webdriver
import unittest

class SearchPython(unittest.TestCase):

    def Setup(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python (self):
        driver = self.driver
        driver.get ("http://python.org")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()