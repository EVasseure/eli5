import click
from bs4 import BeautifulSoup
import urllib2

url = "http://www.reddit.com/r/explainlikeimfive/search?q={query}&restrict_sr=on&sort=top&t=all"


@click.command()
@click.option('--count', default=5, help='Number questions proposed.')
@click.option('--query', prompt='Search',
              help='Your search.')
def hello(count, query):
    """Simple program that greets NAME for a total of COUNT times."""
    response = urllib2.urlopen(url.format(query=query))
    soup = BeautifulSoup(response, 'html.parser')
    results = soup.findAll("div", {"class": "search-result"})
    for i, r in enumerate(results):
        if i == count:
            break
        print("{nb} - {question}".format(nb=i, question=r.div.header.a.string))
    while True:
        try:
            q_nb = int(raw_input("For which question would you like an awswer ?\n"))
            if q_nb < count:
                break
            print("invalid value")
        except ValueError:
            print("invalid value")
    response = urllib2.urlopen(results[q_nb].div.header.a['href'])
    print(results[q_nb].div.header.a['href'])
    # soup = BeautifulSoup(response, 'html.parser')
    # response = soup.findAll("div", {"class": "usertext-body"})
    # print(response[0])

if __name__ == '__main__':
    hello()
