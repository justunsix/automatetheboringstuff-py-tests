import requests
# Library to work with websites: crawling, extracting
from bs4 import BeautifulSoup
import googletrans

# Get webpage
url = "https://dev.to/techworld_with_nana/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths-3gip"
page = requests.get(url)

# Parse HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Get all headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Create a translator
translator = googletrans.Translator()

# Translate headers to Spanish
translated_headers = []
for header in headers:
    # Object / Dictionary to store translated header and HTML tag
    translated_header = {
        "text": translator.translate(header.text, dest='es').text,
        "name": header.name
    }
    
    translated_headers.append(translated_header)

# Write to file
# Use utf-8 encoding to support expected characters
with open('translated_headers.html', 'w', encoding='utf-8') as f:
    f.write("<html><head><title>Translated Headers</title></head><body>\n")
    for header in translated_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')
    f.write("</body></html>\n")