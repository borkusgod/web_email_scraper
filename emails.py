from selenium import webdriver
import time
import re

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'

l = list()
o = {}
target_url = "https://www.randomlists.com/email-addresses"
driver = webdriver.Chrome(PATH)
driver.get(target_url)
time.sleep(10)
driver.close()
