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
from selenium import webdriver 
PATH = "C:/ProgramData/Anaconda3/scripts/chromedriver.exe" #always keeps chromedriver.exe inside scripts to save hours of debugging
driver =webdriver.Chrome(PATH) #preety important part
driver.get("https://www.gharbazar.com/property/search/?_q=&_vt=1&_r=0&_pt=residential&_si=0&_srt=latest")
driver.implicitly_wait(10)
# house=driver.find_elements_by_tag_name("a")
# for lnk in house:
#    print(lnk.get_attribute('href'))
house = driver.find_elements_by_xpath("//div[@id = 'search-properties']/a")
for links in house:
   print(links.get_attribute('href'))










   
#    house_list = []
# for x in house:
#    house_list.append(x.text)
# data = {
#          'Details': house_list,
#          'roads' : house_list
#         }
# df = pd.DataFrame.from_dict(data)
# df.to_csv('housingresult.csv', index = 0)
#this comment should not be visible in another branch....



