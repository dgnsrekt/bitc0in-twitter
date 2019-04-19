import click


@click.group()
def cli():
    "Sync your twitter profile with bitcoins of volatility."


@cli.command()
def run():
    """Run Program"""
    print("RUNNING>>>")


@cli.command()
def test_images():
    """Tests the profile/banner images work."""
    print("TESTING!!!")


if __name__ == "__main__":
    cli()
