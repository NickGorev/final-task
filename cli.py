import click
from pizza import Pizza
import utils


PIZZA_CLASSES = {cls.__name__.lower(): cls for cls in Pizza.__subclasses__()}


@click.group()
def cli():
    pass


@cli.command()
@click.option("-d", "--delivery", default=False, is_flag=True)
@click.option(
    "-s", "--size", type=click.Choice(Pizza.PIZZA_SIZES, case_sensitive=False)
)
@click.argument(
    "pizza",
    nargs=1,
    type=click.Choice(list(PIZZA_CLASSES.keys()), case_sensitive=False),
)
def order(pizza: str, delivery: bool, size: str):
    """Готовит и доставляет пиццу"""
    pizza_class = PIZZA_CLASSES[pizza.lower()]
    pizza_exemplar = pizza_class(size)
    utils.bake(pizza_exemplar)
    if delivery:
        utils.delivery(pizza_exemplar)
    else:
        utils.pickup(pizza_exemplar)


@cli.command()
def menu():
    """Выводит меню"""
    for pizza_class in PIZZA_CLASSES.values():
        click.echo(f"- {pizza_class()}")


if __name__ == "__main__":
    cli()
