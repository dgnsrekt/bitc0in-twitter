import click
from prompt_toolkit import prompt

keivn = "asfd"


@click.group()
def cli():
    """
    Syncs your twitter profile with bitcoin's volatility.
    """


@cli.command()
@click.option("--profile", is_flag=True, help="Changes the profiles picture.")
@click.option("--header", is_flag=True, help="Changes the header.")
@click.option("--color", is_flag=True, help="Changes the profiles color.")
@click.option("--desc", is_flag=True, help="Changes the profiles description.")
@click.option("--suffix", is_flag=True, help="Adds a suffix to the profiles name.")
@click.option("--all", is_flag=True, help="Changes all profile options.")
def run(profile, header, color, desc, suffix, all):
    """Run Program"""
    # will run system check on Run
    # if it cant find env or config file
    # will tell the user to run configure
    print("RUNNING>>>")
    if color:
        print("color")
    if desc:
        print("desc")
    if suffix:
        print("suff")


@cli.command()
def test():
    """Tests the profile/banner images work."""
    print("TESTING!!!")


@cli.command()
def config():
    """Configure the application."""
    print("CONFIGING")
    name = prompt("What is your twitter name?")
    print(name)


if __name__ == "__main__":
    cli()
