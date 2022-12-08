from unittest.mock import patch
from pizza import Margherita, Pepperoni, Hawaiian
from utils import bake, delivery, pickup


def test_bake(capsys):
    with patch("utils.randint") as mocked_randint:
        mocked_randint.return_value = 1
        bake(Margherita())
        captured = capsys.readouterr()
        assert captured.out == "👨‍🍳Приготовили за 1с!\n"
        assert captured.err == ""


def test_delivery(capsys):
    with patch("utils.randint") as mocked_randint:
        mocked_randint.return_value = 2
        delivery(Pepperoni("L"))
        captured = capsys.readouterr()
        assert captured.out == "🛵 Доставили за 2с!\n"
        assert captured.err == ""


def test_pickup(capsys):
    with patch("utils.randint") as mocked_randint:
        mocked_randint.return_value = 5
        pickup(Hawaiian("XL"))
        captured = capsys.readouterr()
        assert captured.out == "🏠 Забрали за 5с!\n"
        assert captured.err == ""
