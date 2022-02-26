#!/usr/bin/python3
import click
import sys

sys.path.append("../")
from functions import years_standings


@click.command()
@click.option(
    "--year",
    prompt=("Enter a year between 2005-2021"),
    help="Get the winner of a specific year",
)
def standings(year: int):
    """Pull the winner of a specific year"""
    response = years_standings(year)
    click.echo(click.style(response, fg="yellow"))


if __name__ == "__main__":
    standings()
