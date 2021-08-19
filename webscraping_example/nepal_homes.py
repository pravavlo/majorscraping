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
# driver.get("https://www.nepalhomes.com/list/&sort=1&find_property_purpose=5db2bdb42485621618ecdae6&find_property_category=5d660cb27682d03f547a6c4a")
driver.implicitly_wait(10)
data_extract= pd.read_csv(r'F:\github projects\homie.csv') #reading csv file which contains 8 links 
de = data_extract['Links'].tolist() #converting the csv file to list so that it can be iterated 
data=[] # created an empty list to store extracted prices after the scraping is done from homie.csv
for url in de[0:]: #de has all the links which i want to iterate and srape prices 
    driver.get(url)
    prices = driver.find_elements_by_xpath("//div[@id='app']/div[1]/div[2]/div[1]/div[2]/div/p[1]")
    name= driver.find_elements_by_xpath("//div[@id='app']/div[1]/div[2]/h1")
    for i in range(len(prices)): 
        data.append([prices[i].text.split('.')[1], name[i].text])
print(data)


df = pd.DataFrame(data, columns = ['price', 'name'])
df.to_csv('nepal_home_value.csv', index = 0)  