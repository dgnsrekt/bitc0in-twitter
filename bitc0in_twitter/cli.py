import click
from core import BitcoinTwitterProfile
from time import sleep
import schedule
import btc


@click.group()
def cli():
    """
    Syncs your twitter profile with bitcoin's volatility.
    """


@cli.command()
def run():
    """Run Program"""
    print("RUNNING>>>")
    bitcoin_percent_change = btc.get_percent_change()
    profile = BitcoinTwitterProfile(bitcoin_percent_change=bitcoin_percent_change)
    print(bitcoin_percent_change)

    def job():
        bitcoin_percent_change = btc.get_percent_change()
        state = profile.get_market_state(bitcoin_percent_change)
        print("state", state, "btc:", bitcoin_percent_change)

        if state == "bearish":
            profile.dumping()
        else:
            profile.pumping()

    schedule.every(10).minutes.do(job)

    while True:
        schedule.run_pending()
        sleep(1)
        print(".", end="", flush=True)


@cli.command()
def test():
    """Tests that all connections work."""
    print("TESTING!!!")
    bms = BitcoinTwitterProfile(bitcoin_percent_change=5)
    bms.dumping()
    print("check the for bearish profile")
    print("state:", bms.state)
    print("Sleeping for 15 seconds.")
    sleep(15)
    bms.pumping()
    print("check the for bullish profile")
    print("state:", bms.state)
    sleep(15)
    bms.dumping()


if __name__ == "__main__":
    cli()
