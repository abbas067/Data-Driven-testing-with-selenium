import xlutils 

import time 

from selenium.webdriver.common.alert import Alert 

from selenium import webdriver 

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe") 

driver.get("http://localhost/stopwatch/index1.php") 

driver.maximize_window() 

path="C:\\Users\logintest.xlsx" 

rows=xlutils.getRowCount(path,"Sheet1") 

for r in range(2,rows+1):# repeat the loop for each row in the xl workbook 

    username=xlutils.readData(path,"Sheet1",r,1)# get username from workbook 

    password=xlutils.readData(path,"Sheet1",r,2)# get password from workbook 

    print(username," ",password) 

    driver.find_element_by_name("fname").send_keys(username) 

    driver.find_element_by_name("pwd").send_keys(password) 

    driver.find_element_by_name("submit").click() 

    if driver.title=="Dashboard": 

        print("test Pass") 

        xlutils.writeData(path,"Sheet1",r,3,"Test Passed") 

        driver.find_element_by_link_text("Logout").click() 

    else: 

        print("test fails") 

        xlutils.writeData(path,"Sheet1",r,3,"Test Failed") 

print(rows) 

driver.close() 
