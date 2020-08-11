import unittest
from selenium import webdriver
import time

class Test(unittest.TestCase):

    def test_Name(self):
        driver = webdriver.Chrome(executable_path="F:\Chethan\STUDY\Installers\Chromedriver for chrome\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        driver.maximize_window()
        time.sleep(4)

        titleOfthePage = driver.title

        self.assertNotEqual("Google",titleOfthePage,"Title of the page is not equals")

        time.sleep(2)

        driver.quit()

if __name__ == "__main__":
    unittest.main()

