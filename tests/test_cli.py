from unittest.mock import patch
from click.testing import CliRunner
import pytest
from cli import menu, order


def test_menu():
    """тестирование вывода меню и интерфейса командной строки"""
    true_result = (
        "- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n"
        + "- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n"
        + "- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n"
    )
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert result.output == true_result


@pytest.mark.parametrize(
    "pizza_name, options, answer",
    [
        ("margherita", [], "🏠 Забрали за 1с!\n"),
        ("pepperoni", ["--delivery"], "🛵 Доставили за 1с!\n"),
        ("hawaiian", ["--size", "L"], "🏠 Забрали за 1с!\n"),
        ("margherita", ["--delivery", "--size", "XL"], "🛵 Доставили за 1с!\n"),
    ],
)
def test_order(pizza_name, options, answer):
    """Тестирование успешных заказов"""
    bake_answer = "👨‍🍳Приготовили за 1с!\n"
    with patch("utils.randint") as mocked_randint:
        mocked_randint.return_value = 1
        runner = CliRunner()
        result = runner.invoke(order, [pizza_name] + options)
        assert result.exit_code == 0
        assert result.output == bake_answer + answer


@pytest.mark.parametrize(
    "pizza_name, options",
    [
        ("margherita_2", []),
        ("pepperoni", ["--delivery home"]),
        ("hawaiian", ["--size", "XXL"]),
        ("pizza", ["--delivery", "--size", "XL"]),
    ],
)
def test_order_wrtong_params(pizza_name, options):
    """тестирование неуспешных заказов"""
    with patch("utils.randint") as mocked_randint:
        mocked_randint.return_value = 1
        runner = CliRunner()
        result = runner.invoke(order, [pizza_name] + options)
        assert result.exit_code != 0
