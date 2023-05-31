import requests
from bs4 import BeautifulSoup


# copy link below
url = 'https://integratedstaffing.ca'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')


# urls = []
redirs_list = []
for link in soup.find_all('a'):
    href_link = link.get('href')
    hl_2str = str(href_link)
    print(url + hl_2str)
    # print(type(hl_2str))
    if hl_2str.startswith('/'):
        # print('redir found')
        if hl_2str not in redirs_list:
            redirs_list.append(href_link)
    # urls.append(href_link)

# for each in urls:
#     print(each)
for each in redirs_list:
    print(each)

