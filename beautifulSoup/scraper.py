from requests_html import HTMLSession

class Scrapper():
  def scrapedata(self, tag):
    url = #f'http://blahblah.com/tag/{tag}'
    s = HTMLSession()
    r = s.get(url)
    print(r.status_code)

    qlist = []
    qoutes = r.html.find('div.quote')
    for q in quotes:
      item = {
        'text': q.find('span.text', first = True).text.strip(),
        'Author': q.find('small.author',first = True).text.strip(),
      }
      print(item)
      qlist.append(item)
  return qlist
  
quotes = Scrapper()
quotes.scrapedata('life')