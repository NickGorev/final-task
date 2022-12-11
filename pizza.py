from typing import List, Optional


class Pizza:
    """базовый класс пицца"""

    PIZZA_SIZES = ["L", "XL"]
    ingredients: List[str] = []
    emoji = ""

    def __init__(self, size: Optional[str] = "L"):
        if size is None:
            size = "L"
        size = size.upper()
        if size not in self.__class__.PIZZA_SIZES:
            raise ValueError(f"size must be in {self.__class__.PIZZA_SIZES}")
        self.size = size

    def dict(self) -> dict:
        """
        возвращает рецепт в виде словаря
        """
        cls = self.__class__
        return {
            "name": cls.__name__,
            "emoji": cls.emoji,
            "ingredients": cls.ingredients,
            "size": self.size,
        }

    def __str__(self) -> str:
        """
        возвращает строковое представление пиццы в виде:
        <название> <иконка>: <список компонентов через запятую>
        """
        recipe = self.dict()
        ingredients_str = ", ".join(recipe["ingredients"])
        return f'{recipe["name"]} {recipe["emoji"]}: {ingredients_str}'

    def __eq__(self, other: object) -> bool:
        """
        проверка пицц на равенство
        """
        return (
            isinstance(other, Pizza)
            and self.size == other.size
            and set(self.ingredients) == set(other.ingredients)
        )


class Margherita(Pizza):
    """пицца маргарита"""

    ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
    emoji = "🧀"


class Pepperoni(Pizza):
    """пицца пеперони"""

    ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
    emoji = "🍕"


class Hawaiian(Pizza):
    """гавайская пицца"""

    ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
    emoji = "🍍"
