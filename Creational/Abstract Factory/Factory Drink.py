from enum import Enum
from abc import ABC, abstractmethod


class Drink(Enum):

    CocaCola = 0
    Fanta = 1
    Sprite = 2



class CreateDrink(ABC):

    def create_drink(self):
        pass


class CreateCola(CreateDrink):

    def create_drink(self):
        print("Your Coca-cola, please!")


class CreateSprite(CreateDrink):

    def create_drink(self):
        print("Your Sprite, please!")


class CreateFanta(CreateDrink):

    def create_drink(self):
        print("Your Fanta, please!")


class FactoryDrink:

    def __init__(self):
        self.factory_dict = {}
        for i, drink in enumerate(Drink):
            method = str(drink).split(".")[1]
            self.factory_dict[i+1] = eval(method)

    def create_drink(self, drink):
        return self.factory_dict[drink]()