import time
from selenium import webdriver 
PATH = "C:/ProgramData/Anaconda3/scripts/chromedriver.exe" #always keeps chromedriver.exe inside scripts to save hours of debugging
driver =webdriver.Chrome(PATH) #preety i,portant part
driver.get("")
languages = driver.find_elements_by_class_name('interlanguage-link') #do it yes 
language_names = [language.find_element_by_css_selector('a').text 
                 for language in languages]

links = [lang.find_element_by_css_selector('a').get_attribute('href') 
        for lang in languages]
content_element = driver.find_element_by_id('n-contents')

content_element.click()
urls = links[0:5] # changes link starting from 0 to 5 link

for url in urls:
    driver.get(url)
    # stop for 2 seconds before going for the next page
    time.sleep(2)
print(links)
print(language_names)
driver.close()