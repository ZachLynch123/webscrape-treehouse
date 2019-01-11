from urllib.request import urlopen
from bs4 import BeautifulSoup

# scrapes whole html document at the highest level (li elements of ul not being displayed)
html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')

soup = BeautifulSoup(html.read(), 'html.parser')

featured_header = soup.find('div', {'class': 'featured'}).h2
print(featured_header)