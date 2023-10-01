import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "https://www.youtube.com"  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract data (modify the selectors as needed)
    article_titles = []
    for article in soup.find_all("article"):
        title_element = article.find("h2")  # Modify this selector to match the actual HTML structure
        if title_element:
            title = title_element.text.strip()
            article_titles.append(title)

    # Print the scraped article titles
    for title in article_titles:
        print(title)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
