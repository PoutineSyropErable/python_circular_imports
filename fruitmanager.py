from typing import TYPE_CHECKING
from typing import List

from fruit import Fruit


if TYPE_CHECKING:
    from .fruit import Fruit


class FruitManager:
    _trackedFruit: List["Fruit"]

    @classmethod
    def init(cls):
        cls._trackedFruit = []

    @classmethod
    def trackFruit(cls, fruit: "Fruit"):
        cls._trackedFruit.append(fruit)
        print(f"Let's say more work is done on fruit {fruit.get_name()}")
        Fruit.sayILoveFruit()

    @classmethod
    def doSomethingOnTrackedFruit(cls):
        for fruit in cls._trackedFruit:
            print(fruit.get_name())
