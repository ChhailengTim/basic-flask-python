import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# Find all h2 elements with class 'post-title'
titles = soup.find_all('h2', {'class':'post-title'})

# Extract and print the text content of each title
for title in titles:
    print(title.text)
