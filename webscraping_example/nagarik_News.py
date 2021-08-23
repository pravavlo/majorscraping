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
driver.get("https://nagariknews.nagariknetwork.com/opinion/604861-1629605867.html")
driver.implicitly_wait(10)
words = []
p10 =driver.find_elements_by_xpath("//div[@id='loy_news_det']/div[1]/div/div/div/div[4]/div/div[1]/div/div[2]/div/article/p[10]")
for x in p10:
    words.append(x.text)
mapped ={
    'sentences': words
}    
df = pd.DataFrame.from_dict(mapped)    
df.to_csv('news.csv', index = 0)


