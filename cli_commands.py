import click
from CLI_Commands import cli_current
from CLI_Commands import cli_standings


@click.group(help="CLI tool to consolidate all my functions")
def cli():
    pass


cli.add_command(cli_current.current)
cli.add_command(cli_standings.standings)

if __name__ == "__main__":
    cli()
