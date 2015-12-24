import click
from bs4 import BeautifulSoup
import urllib2
from cprint import cprint

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
    # print(results[q_nb].div.header.a['href'])

    soup = BeautifulSoup(response, 'html.parser')
    responses = soup.findAll("div", {"class": "entry"})
    question = responses[0].form.div.div
    cprint.warn('\nQuestion:')
    print(question.get_text().replace('  ', ' '))
    i = 1
    while i < len(responses):
        answer = responses[i].form.div.div
        cprint.warn('Answer:')
        print(answer.get_text().replace('  ', ' '))

        if raw_input('Would you like an other answer ? (y/N)') != 'y':
            break
        i += 1

if __name__ == '__main__':
    cprint.warn('Explainlikeimfive\n')
    hello()
