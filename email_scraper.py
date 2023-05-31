from selenium import webdriver
import time
import re

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
l = list()
o = {}
target_url = "https://ormac.ca/contact-us/our-team/"
driver = webdriver.Chrome(PATH)
driver.get(target_url)
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
html = driver.page_source
emails = re.findall(email_pattern, html)
time.sleep(5)
# print(emails)
for each in emails:
    print(each)
# driver.close()
