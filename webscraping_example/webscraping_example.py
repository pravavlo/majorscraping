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
driver.get("https://www.gharghaderi.com/")
driver.implicitly_wait(5)
house = driver.find_elements_by_class_name('griddetails')
for x in house:
   print(x.text)
   house_list = []
house = driver.find_elements_by_class_name('griddetails')
for x in house:
   house_list.append(x.text)
data = {
         'Details': house_list,
         'roads' : house_list
        }
df = pd.DataFrame.from_dict(data)
df.to_csv('housingresult.csv', index = 0)
#



