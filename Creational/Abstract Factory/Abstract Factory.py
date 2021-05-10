from abc import ABC, abstractmethod
from FactoryPizza import FactoryPizza
from FactoryDrink import FactoryDrink


class IAbstractFactory(ABC):

    @abstractmethod
    def create_order(self, order):
        pass


class AbstractFactory(IAbstractFactory):

    def __init__(self):
        self.abstractFactory_dict = {
            1: FactoryPizza,
            2: FactoryDrink
        }
        self.drinks = ["CocaCola", "Fanta","Sprite"]
        self.pizzas = ["Margarita", "Neapolitan", "Marinara"]

    def create_order(self, order):
        if order in self.drinks:
            index = self.drinks.index(order)
            self.abstractFactory_dict[2].create_drink(FactoryDrink(),int(index)+1)
        elif order in self.pizzas:
            index = self.pizzas.index(order)
            self.abstractFactory_dict[1].create_pizza(FactoryPizza(), int(index)+1)
        else:
            print("Error!")
            return "Error"


app = AbstractFactory()
while True:
    temp = input("1 - Pizzas | 2 - Drinks | 3 - exit\n:")
    if temp == "1":
        for i,pizza in enumerate(app.pizzas):
            print(i,"-", pizza)
        order = int(input("Your choose:"))
        app.create_order(app.pizzas[order])
    elif temp == "2":
        for i, drink in enumerate(app.drinks):
            print(i, "-", drink)
        order = int(input("Your choose:"))
        app.create_order(app.drinks[order])
    else:
        print("Bay-bay!")
        break


