import requests
import pdfplumber
from io import BytesIO

def pdf_scraper(url):
    # URL of the PDF file you want to extract text from
    pdf_url = url

# Download the PDF content from the web

    response = requests.get(pdf_url, verify = False)
    pdf_content = response.content

# Create a pdfplumber instance from the downloaded PDF content
    with pdfplumber.open(BytesIO(pdf_content)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text
