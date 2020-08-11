import unittest
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import requests
import datetime
import os
import random

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "G:/Chethan/Python notes/Selenium programs/Pycharm/Screenshots/FAMS/Masters"+timestamp
os.mkdir(path)

class FAMS_aMasters(unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://hublibrt.com:8089"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://hublibrt.com:8089")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_customer_FAMS(self):
        driver = self.driver
        #Sales_date_value = datetime.datetime.now().strftime("%d-%m-%Y")
        Sales_date_value = 24-11-2018
        try:
            self.assertIn("Log in - FAMS", driver.title)
            time.sleep(3)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.User_name.clear()
            self.password.clear()

            try :
                self.Financial_year = driver.find_element_by_xpath("//*[@class='control-label required']")
                select_financial = Select(driver.find_element_by_name('FinancialYearId'))
                select_financial.select_by_value('b0cN2xK0dEuB5IiPBJhdeA')
                time.sleep(5)
                self.Division = driver.find_element_by_xpath("//*[@class='form-control division']")
                select_Division = Select(driver.find_element_by_name('DivisionId'))
                select_Division.select_by_value('YzdApSYEAkG4uOFXtRYKBg')
                time.sleep(3)
                self.User_name.send_keys("operator")
                self.password.send_keys("password")
                self.assertIn("Financial Accounting Management System", driver.page_source)
                print ("Validation of Master tab is successful")
                self.submit = driver.find_element_by_xpath("//*[@class='btn btn-primary btn-group-justified']").click()
                time.sleep(10)
                self.menu = driver.find_element_by_xpath("//*[@class='menu-toggler']").click()
                time.sleep(4)
                self.customer = driver.find_element_by_xpath("//*[@data-original-title='Customer']").click()
                time.sleep(8)
                self.sales_order = driver.find_element_by_xpath("//*[@data-original-title='Sales Order']").click()
                time.sleep(4)
                #driver.get_screenshot_as_file(path + "/" + "Sales_order" + timestamp + ".png")
                time.sleep(6)
                self.Sales_order_creation = driver.find_element_by_xpath("//*[@class='btn btn-primary show-modal']").click()
                time.sleep(4)
                num = random.randint(1,100)
                Sales_number = 'SO' + str(num)
                print("sales order number : ",Sales_number)
                self.sales_order_number = driver.find_element_by_id("SaleOrderNo").send_keys(Sales_number)
                time.sleep(4)

                self.Sales_date = driver.find_element_by_xpath("//*[@class='form-control date']").click()
                value = driver.find_element_by_xpath("//*[@class='form-control date']").get_attribute('value')
                print(value)

                driver.find_element_by_xpath("//*[@class='dtp-btn-ok btn btn-flat btn-xs']").click()
                time.sleep(2)
                value1 = driver.find_element_by_xpath("//*[@class='form-control date']").get_attribute('value')
                print(value1)
                
                driver.find_element_by_xpath("//*[@class='chosen-container chosen-container-single']").click()
                print("In stage 1")
                dropdown1 = driver.find_element_by_xpath("//*[@class='chosen-drop']")
                print("In stage 2")
                '''
                dropdown2 = dropdown1.find_element_by_xpath("//*[@class='chosen-results']")
                Result = dropdown2.find_elements_by_tag_name('li')
                for items in Result:
                    text = items.text
                    print(text)
                
                driver.find_element_by_xpath("//*[@class='control-label required']")
                select_BillTo = Select(driver.find_element_by_id('BillTo'))
                select_BillTo.select_by_value('R0maW66WME2hw1gSIZct3Q')
                time.sleep(4)
                '''
                cust_job = 'ticket'
                print("Ticketing")
                self.cust_date1 = driver.find_element_by_id("Job").send_keys(cust_job)
                time.sleep(2)
                cust_reason = 'Ticketing'
                self.cust_reason1 = driver.find_element_by_id("Reason").send_keys(cust_reason)
                time.sleep(2)
                self.addrow = driver.find_element_by_id("AddRow").click()
                time.sleep(2)
                cust_item = 'Barrings'
                self.add_items = driver.find_element_by_id("SODetail_0__Item").send_keys(cust_item)
                time.sleep(2)
                '''
                self.Cust_type = driver.find_element_by_id('SODetail_0__Type')
                select_type = Select(driver.find_element_by_name('SODetail[0].Type'))
                select_type.select_by_value('1')
                '''
                HSN_Value = 'HSN9909'
                self.HSN_value = driver.find_element_by_id('SODetail_0__HSNCode').send_keys(HSN_Value)
                time.sleep(2)
                Cust_quantity = 1
                driver.find_element_by_id('SODetail_0__Quantity').clear()
                driver.find_element_by_id('SODetail_0__Quantity').send_keys(Cust_quantity)
                time.sleep(3)
                Cust_price = 1000
                driver.find_element_by_id('SODetail_0__Price').clear()
                driver.find_element_by_id('SODetail_0__Price').send_keys(Cust_price)
                time.sleep(3)
                driver.find_element_by_id('SODetail_0__Total').click()
                time.sleep(3)
                driver.find_element_by_id('SODetail_0__SubTotal').click()
                time.sleep(4)

                driver.find_element_by_xpath("//*[@class='glyphicon glyphicon-save-file']").click()
                time.sleep(5)
                print("Validation of FAMS Customer tab is pass")

            except AssertionError:
                print ("Login failed : Invalid Username and Password")
        except AssertionError:
             print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)