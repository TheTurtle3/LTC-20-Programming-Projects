import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

title = soup.find_all('h2', {'class': 'post-title'})
print(title[0].getText())