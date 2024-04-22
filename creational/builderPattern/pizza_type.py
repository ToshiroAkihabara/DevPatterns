from enum import Enum, auto
from collections import namedtuple


pizza_base = namedtuple('Pizza', ['DoughDepth', 'DoughType'])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RVE = auto()


class PizzaSauces(Enum):
    PESTO = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopping(Enum):
    MOZZARELLA = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()
    TOMATO = auto()