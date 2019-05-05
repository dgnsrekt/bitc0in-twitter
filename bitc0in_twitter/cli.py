import click
from core import BitcoinTwitterProfile
from time import sleep


@click.group()
def cli():
    """
    Syncs your twitter profile with bitcoin's volatility.
    """


@cli.command()
def run():
    """Run Program"""
    print("RUNNING>>>")


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


if __name__ == "__main__":
    cli()
