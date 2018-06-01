from selenium import webdriver
from selenium.webdriver.common.keys
import random 
def googlesearch(): 
    newtab = 0
    while True:
        
        if newtab != 0: 
            driver = webdriver.Firefox() 
            driver.get("https://www.google.com")
            timeout = 20
            query = random.choice(list(open('google.txt')))
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(query)
            input_element.submit()
            browser.close() 
        elif newtab < 6: # firefox is already open, and we have less than 6 tabs
            driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
            driver.get("https://www.google.com")
            timeout = 20
            query = random.choice(list(open('google.txt')))
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(query)
            input_element.submit()
            newtab = newtab + 1 

