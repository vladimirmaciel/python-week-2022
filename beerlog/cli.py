# import sys

# from .config import settings


# def main():
#     # print("Hello from", settings.NAME)
#     for attr in sys.argv[1:]:
#         print("->", attr)

from typing import List, Optional

#  cria interface de CLI e utiliza anotações de tipos
import typer
from rich.console import Console
from rich.table import Table

from beerlog.core import add_berr_to_database, get_beers_from_database

main = typer.Typer(help="Beer Management Application")
console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):

    """Adds a new beer to database."""
    if add_berr_to_database(name, style, flavor, image, cost):
        print("Beer added to database")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """List beer in database"""
    beers = get_beers_from_database()
    # print(beers)
    table = Table(title="Beerlog :beer_mug:")
    headers = ["id", "name", "style", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
