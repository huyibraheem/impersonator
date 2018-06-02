from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup 
import re 
from urllib.request import urlopen
import random 
def googlesearch(): 
    newtab = 0
    while True:
        if newtab == 0: 
            driver = webdriver.Firefox() 
            driver.get("https://www.google.com")
            timeout = 20
            query = random.choice(list(open('google.txt')))
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(query)
            input_element.submit()
            newtab = newtab + 1
        elif newtab < 6 and newtab != 0: # firefox is already open, and we have less than 6 tabs
            r = random.randint(1,2) # choose between opening new tab or following links 
            if r == 1: 
                driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
                driver.get("https://www.google.com")
                timeout = 20
                query = random.choice(list(open('google.txt')))
                input_element = driver.find_element_by_name("q")
                input_element.send_keys(query)
                input_element.submit()
                newtab = newtab + 1
            elif r == 2:
                links = []
                interval = random.randint(20, 100) # sleep interval for clicking 
                html = urlopen(driver.current_url)
                soup = BeautifulSoup(html)
                for i in soup.findAll('a', attrs={'href': re.compile("^http://")}): 
                    links.append(i.get('href'))
                goto = random.choice(links)
                driver.get(goto)
