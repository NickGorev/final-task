# Финальный проект по курсу python

Сервис по приготовлению и доставке пиццы.

Файл [pizza.py](pizza.py) содержит базовый класс пиццы и три класса конкретных пицц. Файл [utils.py](utils.py) содержит функции, имитирующие приготовление, доставку и самовывоз пиццы. Файл [cli.py](cli.py) содержит реализацию интерфейса командной строки. В папке [tests](./tests) содержатся тесты.

Можно заказать пиццу трёх видов: `Margherita`,  `Pepperoni` и `Hawaiian`. Размер пиццы может быть `L` либо `XL`.

## Интерфейс командной строки
Для просмотра доступного меню используется команда `menu`:
```console
$ python cli.py menu
- Margherita 🧀: tomato sauce, mozzarella, tomatoes
- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni
- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples
```
Для заказа пиццы используется команда `order`:
```console
$ python cli.py order {margherita|pepperoni|hawaiian} [OPTIONS]
```
Опции:

`--delivery` - флаг доставки, по умолчанию доставка не требуется, самовывоз.

`--size [L|XL]` - размер пиццы, по умолчанию выбирается размер `L`.
### Примеры
```console
$ python cli.py order pepperoni
👨‍🍳Приготовили за 22с!
🏠 Забрали за 78с!
```
```console
$ python cli.py order margherita --delivery
👨‍🍳Приготовили за 62с!
🛵 Доставили за 78с!
```
```console
$ python cli.py order margherita --delivery
👨‍🍳Приготовили за 62с!
🛵 Доставили за 78с!
```
```console
python cli.py order hawaiian --delivery --size XL
👨‍🍳Приготовили за 73с!
🛵 Доставили за 85с!
```
## Запуск тестов
Для запуска тестов выполняется команда
```console
$ python -m pytest -v tests/
```
Либо, если требуется отчёт в формате HTML:
```console
$ python -m pytest -v tests/ --cov --cov-report html
```
