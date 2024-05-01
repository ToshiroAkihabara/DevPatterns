from abc import ABC, abstractmethod
from pizza_type import pizza_base, PizzaDoughDepth, PizzaTopping, PizzaSauces, PizzaDoughType
from pizza_base import Pizza


class Builder(ABC):
    @abstractmethod
    def prepare_dough(self) -> None:
        pass

    @abstractmethod
    def add_sauce(self) -> None:
        pass

    @abstractmethod
    def add_topping(self) -> None:
        pass

    @abstractmethod
    def get_pizza(self) -> None:
        pass


class MargaritaPizza(Builder):
    def __init__(self):
        self.pizza = Pizza("Margarita")
        self.pizza.cooking_time = 15

    def prepare_dough(self) -> None:
        self.pizza.dough = pizza_base(PizzaDoughDepth.THIN, PizzaDoughType.WHEAT)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauces.TOMATO

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                i for i in (PizzaTopping.MOZZARELLA,
                            PizzaTopping.MOZZARELLA,
                            PizzaTopping.BACON)
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


class CheesePizza(Builder):
    def __init__(self):
        self.pizza = Pizza("Cheese")
        self.pizza.cooking_time = 10

    def prepare_dough(self) -> None:
        self.pizza.dough = pizza_base(PizzaDoughDepth.THICK, PizzaDoughType.CORN)

    def add_sauce(self) -> None:
        self.pizza.sauce = PizzaSauces.CHEESE

    def add_topping(self) -> None:
        self.pizza.topping.extend(
            [
                i for i in (PizzaTopping.MOZZARELLA,
                            PizzaTopping.MOZZARELLA,
                            PizzaTopping.TOMATO)
            ]
        )

    def get_pizza(self) -> Pizza:
        return self.pizza


