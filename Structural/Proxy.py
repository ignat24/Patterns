from abc import ABC, abstractmethod

from functools import partial

class AbstractCar:

    # @classmethod
    # def create(cls, name):
    #     return cls(name)

    def add_option(self,option):
        raise NotImplemented()

    def paint_color(self, color):
        raise NotImplemented()

    def save_config(self, configName):
        raise NotImplemented()


class Car(AbstractCar):

    def __init__(self, name):
        self._name = name

    def add_option(self, option):
        print("Add option -", option)

    def paint_color(self, color):
        print("Paint in", color)

    def save_config(self, configName):
        print("Config name is -", configName)



class CarProxy(AbstractCar):

    def __init__(self, name):
        self._car = Car(name)
        self.options = []

    def add_option(self, *args):
        func = partial(self._car.add_option, *args)
        self.options.append(func)

    def paint_color(self, *args):
        func = partial(self._car.paint_color, *args)
        self.options.append(func)

    def save_config(self, configName):
        for i in range(len(self.options)):
            self.options[i]()
        # map(lambda f: f(), self.options)
        # self.options[0]()
        self._car.save_config(configName)


car = CarProxy("Audi")
car.add_option("Cruise Control")
car.add_option("ABS")
car.paint_color("Red")
car.save_config("Comfort")




