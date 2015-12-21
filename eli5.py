import click
from bs4 import BeautifulSoup
import urllib2

url = "http://www.reddit.com/r/explainlikeimfive/search?q={query}&restrict_sr=on&sort=top&t=all"


@click.command()
@click.option('--count', default=1, help='Number of answers.')
@click.option('--query', prompt='Search',
              help='Your search.')
def hello(count, query):
    """Simple program that greets NAME for a total of COUNT times."""
    print(query)
    response = urllib2.urlopen(url.format(query=query))
    soup = BeautifulSoup(response, 'html.parser')
    results = soup.findAll("div", {"class": "search-result"})
    for r in results:
        print(r.div.header.a.string.replace("ELI5:", ""))

if __name__ == '__main__':
    hello()
