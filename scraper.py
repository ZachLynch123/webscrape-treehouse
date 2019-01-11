from urllib.request import urlopen
from bs4 import BeautifulSoup

# scrapes whole html document at the highest level (li elements of ul not being displayed)
html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')

soup = BeautifulSoup(html.read(), 'html.parser')

# since class is a reserved word in pyton, bs4 uses class_ to differentiacte between the two
""" for button in soup.find(class_='button button--primary'):
    print(button) """
# finds all internal and external links in the webpage's ancher tags
for link in soup.find_all('a'):
    print(link.get('href'))