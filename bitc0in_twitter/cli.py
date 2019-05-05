import click


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
    """Tests the profile/banner images work."""
    print("TESTING!!!")


@cli.command()
@click.option("--clean", is_flag=True, help="Generates clean config file.")
def config(clean):
    """Configure the application."""
    print("CONFIGING")
    name = prompt("What is your twitter name?")
    print(name)


if __name__ == "__main__":
    cli()
