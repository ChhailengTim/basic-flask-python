import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.facebook.com'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Find all the links on the page
        links = soup.find_all('a')

        # Print the extracted links
        for link in links:
            href = link.get('href')
            if href:
                print(href)
    else:
        print('Failed to retrieve the web page:', response.status_code)

except Exception as e:
    print('An error occurred:', str(e))

