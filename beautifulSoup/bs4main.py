#beautifulSoup practice
##html scraping
from bs4 import BeautifulSoup

with open('file.html', 'r') as html_file: 
  content = html_file.read()
  print(content) ## this will print literally html itself
  
  soup = BeautifulSoup(content, 'lxml')
  print(soup.prettify())
  
  tags = soup.find('h5')
  print(tag)
  for course in courses:
    print(course.text)

##