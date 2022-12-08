import pytest
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


def test_pizza():
    generic_pizza = Pizza()
    pizza_dict = generic_pizza.dict()
    exp_dict = {"name": "Pizza", "emoji": "", "ingredients": [], "size": "L"}
    assert pizza_dict == exp_dict


def test_pizza_xl():
    generic_pizza = Pizza("XL")
    pizza_dict = generic_pizza.dict()
    exp_dict = {"name": "Pizza", "emoji": "", "ingredients": [], "size": "XL"}
    assert pizza_dict == exp_dict


def test_pizza_wring_size():
    with pytest.raises(ValueError) as err:
        Pizza("XXL")

    print(err.value.args[0])
    assert err.value.args[0] == "size must be in ['L', 'XL']"


def test_margherita():
    pizza = Margherita()
    pizza_dict = pizza.dict()
    exp_dict = {
        "name": "Margherita",
        "emoji": "🧀",
        "ingredients": ["tomato sauce", "mozzarella", "tomatoes"],
        "size": "L",
    }
    assert pizza_dict == exp_dict
    assert str(pizza) == "Margherita 🧀: tomato sauce, mozzarella, tomatoes"


def test_pepperoni():
    pizza = Pepperoni("L")
    pizza_dict = pizza.dict()
    exp_dict = {
        "name": "Pepperoni",
        "emoji": "🍕",
        "ingredients": ["tomato sauce", "mozzarella", "pepperoni"],
        "size": "L",
    }
    assert pizza_dict == exp_dict
    assert str(pizza) == "Pepperoni 🍕: tomato sauce, mozzarella, pepperoni"


def test_hawaiian():
    pizza = Hawaiian("XL")
    pizza_dict = pizza.dict()
    exp_dict = {
        "name": "Hawaiian",
        "emoji": "🍍",
        "ingredients": ["tomato sauce", "mozzarella", "chicken", "pineapples"],
        "size": "XL",
    }
    assert pizza_dict == exp_dict
    assert str(pizza) ==\
        "Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples"


@pytest.mark.parametrize(
    "first_pizza, second_pizza, result",
    [
        (Pizza(), Pizza(), True),
        (Pizza(), Pizza("L"), True),
        (Pizza("L"), Pizza(), True),
        (Pizza("L"), Pizza("L"), True),
        (Pizza("XL"), Pizza("XL"), True),
        (Pizza("L"), Pizza("XL"), False),
        (Pizza("XL"), Pizza(), False),
        (Margherita(), Margherita(), True),
        (Pepperoni("L"), Pepperoni("L"), True),
        (Hawaiian("XL"), Hawaiian("XL"), True),
        (Margherita("L"), Margherita("XL"), False),
        (Margherita(), Pepperoni(), False),
        (Margherita("L"), Hawaiian("L"), False),
        (Pepperoni(), Margherita(), False),
        (Pepperoni("XL"), Hawaiian("XL"), False),
        (Hawaiian(), Margherita(), False),
        (Hawaiian(), Pepperoni(), False),
        (Hawaiian(), 123, False),
        (Hawaiian(), "Hawaiian", False),
    ],
)
def test_pizza_eq(first_pizza, second_pizza, result):
    assert (first_pizza == second_pizza) == result
