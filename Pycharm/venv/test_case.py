from selenium import webdriver
import unittest

class SearchPython(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_python(self):
        self.driver.get("http://python.org")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()