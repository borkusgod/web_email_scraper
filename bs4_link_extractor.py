import requests
from bs4 import BeautifulSoup

# paste in address below
url = 'https://integratedstaffing.ca'

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

link_check_cont = []
for link in soup.find_all('a'):
    # convert links into strings for appending to list
    redirs = str(link.get('href'))
    if redirs.startswith('/'):
        home_link = url + redirs
        if home_link not in link_check_cont:
            link_check_cont.append(home_link)

# display links from search
for each in link_check_cont:
    print(each)

