from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
clms = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

print(rows,clms)

time.sleep(2)

for row in range(1, rows + 1):
    for colms in range(1,clms + 1):
        print("Column : ", colms)
        print("Row : ", row)
        time.sleep(2)
        value = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(row)+"]/th["+str(colms)+"]").text
        print(value, end='                   ')
        time.sleep(2)
    print()

driver.quit()