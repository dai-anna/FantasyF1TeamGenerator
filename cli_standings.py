#!/usr/bin/python3
import click
from functions import years_standings, current_standings


@click.command()
@click.option(
    "--standings",
    prompt=("Enter a year between 2005-2021"),
    help="Get the winner of a specific year",
)
def standings(year: int):
    """Pull the winner of a specific year"""
    response = years_standings(year)
    click.echo(response)


def current():
    """Pull the current year's winner"""
    response = current_standings()
    click.echo(response)


if __name__ == "__main__":
    current()
    # standings()
