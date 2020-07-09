from cli import bitc0in_twitter

import click

from logo import LOGO


def main():
    click.echo(LOGO)
    bitc0in_twitter()


if __name__ == "__main__":
    main()
