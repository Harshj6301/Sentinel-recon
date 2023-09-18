import requests
from bs4 import BeautifulSoup


def scrape(url):
    # URL of the webpage you want to scrape
    URL = url

    PARAGRAPHS = []
    LINKS = []

    # Send a GET request to the webpage
    response = requests.get(URL)
    response.raise_for_status()  # Check for errors

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract and print the title of the webpage
    title = soup.title.text
    print(f"Title: {title}")

    # Extract and print all the paragraph text on the webpage
    paragraphs = soup.find_all("p")
    for idx, paragraph in enumerate(paragraphs, start=1):
        print(f"Paragraph {idx}: {paragraph.text.strip()}")
        PARAGRAPHS.append(paragraph.text.strip())

    # Extract and print all the links on the webpage
    links = soup.find_all("a")
    for idx, link in enumerate(links, start=1):
        href = link.get("href")
        print(f"Link {idx}: {href}")
        LINKS.append(href)
    
    return PARAGRAPHS, LINKS