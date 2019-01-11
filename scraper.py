from urllib.request import urlopen
from bs4 import BeautifulSoup

# scrapes whole html document at the highest level (li elements of ul not being displayed)
html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')

soup = BeautifulSoup(html.read(), 'html.parser')

featured_header = soup.find('div', {'class': 'featured'})
print(featured_header.get_text())

# find methon only finds the first, or specific element, find all finds all elements

# parameters: name: name of element
# attrs: looks for specific css class
# recursive: all instences of tags. setting recursive to false will find only the direct children of the tag
# string searches for strings rather than tags
# **kwargs: searching out other items like css ids
# limit: limits amount returned. for example, find is find_all with a limit of 1