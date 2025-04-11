from fruitmanager import FruitManager


class Fruit:
    def __init__(self, name: str):
        self._name = name
        FruitManager.trackFruit(self)

    def get_name(self) -> str:
        return self._name

    @classmethod
    def sayILoveFruit(cls):
        print("I love fruit")
