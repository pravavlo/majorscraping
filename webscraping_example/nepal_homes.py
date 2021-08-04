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
home_links=[]
def isDisplayed():
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div[3]/button')
    except NoSuchElementException:
        return(False)
    return True
while(isDisplayed):
        try:
            nepahome_links=driver.find_elements_by_xpath("//div[@id='app']/div[1]/div/div/div/div[2]/div[3]/a")
            for ele in nepahome_links:
                home_links.append(ele.get_attribute('href'))
            show_more_listings = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/div[3]/button')
            show_more_listings.click()
            time.sleep(1)       
        except:
            break

print(len(home_links))
for i in range(len(home_links)):
    print(home_links[i]) 
data = {
    'Links':home_links 
    }
df = pd.DataFrame.from_dict(data)
df.to_csv('nepal_homes_links.csv', index = 0)  
driver.quit()