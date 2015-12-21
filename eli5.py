import click


@click.command()
@click.option('--count', default=1, help='Number of answers.')
@click.option('--name', prompt='Search',
              help='Your search.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        print(name)

if __name__ == '__main__':
    hello()
