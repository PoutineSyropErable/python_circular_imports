from .fruit import Fruit
from .fruitmanager import FruitManager


FruitManager.init()
fruit = Fruit("Apple")

FruitManager.doSomethingOnTrackedFruit()
exit(0)
