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


class Factory:

    def __init__(self):
        self.factory_dict={}
        # self.factory_dict = {1: Margarita,
        #                     2: Neapolitan,
        #                     3: Marinara}
        for i,pizza in enumerate(PizzaType):
            method = str(pizza).split(".")[1]
            self.factory_dict[i+1] = eval(method)


    def create_pizza(self, pizzaType):
        return self.factory_dict[pizzaType]()


class PizzaStore:

    def __init__(self):
        self.factory = Factory()

    def buy_pizza(self, pizzaType):
        concretePizza = self.factory.create_pizza(pizzaType)
        print("You order:", self.factory.factory_dict[pizzaType], "price =", concretePizza.get_price())


pizzaStore = PizzaStore()
while True:
    for i, pizza in enumerate(PizzaType):
        print(i+1,"-", pizza)
    temp = input("Your order:")
    if int(temp) < 4:
        pizzaStore.buy_pizza(int(temp))
    else:
        print("Good day!")
        break
    print("\n")






