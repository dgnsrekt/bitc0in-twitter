import nox


@nox.session
def tests(session):
    """Running tests."""
    session.install("pipenv")
    session.run("pipenv", "install", "--dev")
    session.run("pipenv", "run", "pytest", "--disable-warnings")


@nox.session
def lint(session):
    """Linting using black/flake8"""
    session.install("flake8", "flake8-import-order", "black")
    session.run("black", "--line-length", "99", "--check", ".")
    session.run("flake8", "bitc0in_twitter")
