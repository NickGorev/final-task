from functools import wraps
from typing import Callable
from random import randint

from pizza import Pizza


def log(format_str: str) -> Callable:
    """генерирует декоратор, который выводит время выполнения
    format_str: шаблон, в который подставляется время
    """

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args, **kwargs):
            return_value = function(*args, **kwargs)
            print(format_str.format(randint(a=1, b=100)))
            return return_value

        return wrapper

    return decorator


@log("👨‍🍳Приготовили за {}с!")
def bake(pizza: Pizza) -> None:
    """Готовит пиццу"""
    pass


@log("🛵 Доставили за {}с!")
def delivery(pizza: Pizza) -> None:
    """Доставляет пиццу"""
    pass


@log("🏠 Забрали за {}с!")
def pickup(pizza: Pizza) -> None:
    """Самовывоз"""
    pass
