#!/usr/bin/python3
import click
import sys

sys.path.append("../")
from functions import current_standings


@click.command()
def current():
    """Pull the current year's winner"""
    response = current_standings()
    click.echo(click.style(response, fg="yellow"))


if __name__ == "__main__":
    current()
