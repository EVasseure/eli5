import click
from bs4 import BeautifulSoup
import requests
from cprint import cprint

url = "http://www.reddit.com/r/explainlikeimfive/search?q={query}&restrict_sr=on&sort=top&t=all"


@click.command()
@click.option('--count', default=5, help='Number questions proposed.')
@click.option('--query', prompt='Search', help='Your search.')
def hello(count, query):
    response = requests.get(url.replace("{query}", query))
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.findAll("div", {"class": "search-result"})

    for r in results[:count]:
        print("{nb} - {question}".format(nb=i, question=r.div.header.a.string))
    while True:
        try:
            q_nb = int(input("For which question would you like an awswer ?\n"))
            if q_nb < count:
                break
            print("invalid value")
        except ValueError:
            print("invalid value")
    response = requests.get(results[q_nb].div.header.a['href'])

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

        if input('Would you like an other answer ? (y/N)') != 'y':
            break
        i += 1

if __name__ == '__main__':
    cprint.warn('Explainlikeimfive\n')
    hello()
