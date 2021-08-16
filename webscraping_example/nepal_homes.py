from logging import exception
from typing import Text
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv
import re
from selenium import webdriver 
PATH = "C:/ProgramData/Anaconda3/scripts/chromedriver.exe" #always keeps chromedriver.exe inside scripts to save hours of debugging
driver =webdriver.Chrome(PATH) #preety important part
driver.get("https://www.nepalhomes.com/list/&sort=1&find_property_purpose=5db2bdb42485621618ecdae6&find_property_category=5d660cb27682d03f547a6c4a")
driver.implicitly_wait(10)
data_extract= pd.read_csv(r'F:\github projects\homie.csv')
de = data_extract['Links'].tolist()
data=[]
price=[]
for i in range(0,9):
    final = de[i]
    try:
        price =driver.get_elements_by_xpath('text-3xl font-bold leading-none text-black')
    except:
        print("none") 
    price.text
    print(price)  

    
    

    





















# home_links=[]
# try:
#     nepahome_links=driver.find_elements_by_xpath("//div[@id='app']/div[1]/div/div/div/div[2]/div[3]/a")
#     for ele in nepahome_links:
#         home_links.append(ele.get_attribute('href'))   
# except NoSuchElementException:
#     print("end")

# print(len(home_links))
# for i in range(len(home_links)):
#     print(home_links[i]) 
# data = {
#     'Links':home_links 
#     }
# df = pd.DataFrame.from_dict(data)
# df.to_csv('homie.csv', index = 0, header=True)  
# driver.quit()