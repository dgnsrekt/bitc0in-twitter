from time import sleep

import btc

import click

from core import BitcoinTwitterProfile

import schedule


@click.group()
def bitc0in_twitter():
    """
    Syncs your twitter profile with bitcoin's volatility.
    """


@bitc0in_twitter.command()
def run():
    """Start Program"""
    bitcoin_percent_change = btc.get_percent_change()
    profile = BitcoinTwitterProfile(bitcoin_percent_change=bitcoin_percent_change)

    def job():
        bitcoin_percent_change = btc.get_percent_change()
        state = profile.get_market_state(bitcoin_percent_change)

        if state == "bearish":
            profile.dumping()
        else:
            profile.pumping()

    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        sleep(1)
        # print(".", end="", flush=True)


@bitc0in_twitter.command()
def test():
    """Tests everything is setup correctly."""
    click.echo("TESTING!!!")
    bms = BitcoinTwitterProfile(bitcoin_percent_change=5)
    bms.dumping()
    click.echo("check the for bearish profile")
    click.echo(f"state: {bms.state}")
    click.echo("Sleeping for 15 seconds.")
    sleep(15)
    bms.pumping()
    click.echo("check the for bullish profile")
    click.echo(f"state: {bms.state}")
    sleep(15)
    bms.dumping()


if __name__ == "__main__":
    bitc0in_twitter()
