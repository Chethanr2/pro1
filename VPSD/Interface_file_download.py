import unittest
from urllib.request import urlopen
from selenium import webdriver
import zipfile
import time
import requests
import datetime
import os
import shutil

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
path = "F:/Chethan/STUDY/Python notes/Selenium programs/Pycharm/Screenshots/Interface_file"+timestamp
os.mkdir(path)
zip_files = []

class VPSD_eInterface_Tab(unittest.TestCase):

    def setUp(self):
        try:
            stri = "http://nechubli.com:2001"
            self.data = urlopen(stri)
            print ("Internet is working")
            self.driver = webdriver.Chrome()
            self.driver.set_page_load_timeout(120)
            self.driver.maximize_window()
            self.driver.implicitly_wait(60)
            self.driver.get("http://nechubli.com:2001")

        except requests.ConnectionError as e:
            print ("not connected :",e)

    def test_login_VPSD(self):
        driver = self.driver
        try:
            self.assertIn("VPSD System", driver.title)
            self.User_name = driver.find_element_by_id("UserName")
            self.password = driver.find_element_by_id("Password")
            self.submit = driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary btn-default']")
            self.User_name.clear()
            self.password.clear()

            try :
                self.User_name.send_keys("VPSD")
                self.password.send_keys("Vpsd_master@321")
                self.submit.click()
                self.assertIn("Vehicle Planning and Scheduling System", driver.page_source)
                time.sleep(10)
                print ("Testing Interface file download")
                time.sleep(5)
                self.submit1 = driver.find_element_by_xpath("//span[@class='scoop-mtext' and text() = 'Interfaces']")
                self.submit1.click()
                time.sleep(5)
                driver.get_screenshot_as_file(path +"/"+ "Interface_menu" + timestamp + ".png")
                time.sleep(4)

                print("Validating the interface files download option is working fine or not")
                # To verify the download option is working successfully
                driver.find_element_by_xpath("//*[@class='btn  btn-primary']").click()
                timestamp1 = datetime.datetime.now().strftime("%m%d%y%H%M")
                time.sleep(40)
                print ("Timestamp1 = ",timestamp1)
                driver.get_screenshot_as_file(path+"/" + "Interface_files_download" + timestamp + ".png")
                time.sleep(4)

                my_file = 'C:\\users\\chethan.r\\downloads'
                lists = os.listdir(my_file)
                ff = []
                time.sleep(4)
                for files in lists:
                    if files.endswith(".zip"):
                        if files.startswith("Interface"):
                            f = files
                            zip_files.append(f)
                            time.sleep(1)

                for filess in zip_files:
                    if timestamp1 in filess:
                        ff = filess
                        print("Interface file =",ff)

                if not ff:
                    print("File download Fails")
                    exit(0)
                else:
                    print("File download successful")
                    src = "C:\\users\\chethan.r\\downloads\\" + ff
                    os.mkdir("C:\\users\\chethan.r\\Desktop\\Interface_files")
                    dst = "C:\\users\\chethan.r\\Desktop\\Interface_files\\"
                    shutil.copy(src, dst)
                    File_name = dst + ff
                    zip_ref = zipfile.ZipFile(File_name, 'r')
                    zip_ref.extractall(dst)
                    zip_ref.close()

                    Inter_list = os.listdir(dst)
                    number_files = len(Inter_list)
                    print("Number of files in the interface zip : ", number_files)

                    lists = os.listdir(dst)

                    zip_filess = []

                    for files in lists:
                        if files.endswith(".csv"):
                            f = files
                            zip_filess.append(f)

                    count = 0
                    choped_files = []

                    for filesss in zip_filess:
                        ff = filesss.split("_")[0]
                        choped_files.append(ff)

                    for ch in choped_files:
                        if ch == 'Stop':
                            print("stop file is present")
                            count = count + 1
                        elif ch == 'StopOnRoute':
                            print("stop on route file is present")
                            count = count + 1
                        elif ch == 'StopDistance':
                            print("stop distance file is present")
                            count = count + 1
                        elif ch == 'Schedule':
                            print("schedule file is present")
                            count = count + 1
                        elif ch == 'ScheduleForRoute':
                            print("schedule for route files are present")
                            count = count + 1
                        elif ch == 'ScheduleForStopOnRoute':
                            print("Schedule For Stop on route file is present")
                            count = count + 1
                        elif ch == 'Route':
                            print("Route file is present")
                            count = count + 1

                    if count == 7:
                        print("Downloaded zip files are having all the master files")
                    else:
                        print("Downloaded zip file is not having all the master files")

            except AssertionError:
                print("Login failed : Invalid Username and Password")
        except AssertionError:
            print("Hitting wrong URL")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)