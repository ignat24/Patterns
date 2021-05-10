from abc import ABC, abstractmethod

from enum import Enum


class PizzaType(Enum):

    Margarita = 0
    Neapolitan = 1
    Marinara = 2


class Pizza:

    def __init__(self, price):
        self.__price = price

    def get_price(self,):
        return self.__price


class Margarita(Pizza):

    def __init__(self):
        super().__init__(5)


class Neapolitan(Pizza):

    def __init__(self):
        super().__init__(7)


class Marinara(Pizza):

    def __init__(self):
        super().__init__(10)


class FactoryPizza:

    def __init__(self):
        self.factory_dict={}
        # self.factory_dict = {1: Margarita,
        #                     2: Neapolitan,
        #                     3: Marinara}
        for i,pizza in enumerate(PizzaType):
            method = str(pizza).split(".")[1]
            self.factory_dict[i+1] = eval(method)


    def create_pizza(self, pizzaType):
        pizza = self.factory_dict[pizzaType]()
        print("Your pizza", pizza, "price:", pizza.get_price())





