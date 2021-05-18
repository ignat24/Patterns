

class Car:
    def template_method(self):
        self.engine()
        self.power()
        self.coast()

    def engine(self):
        pass

    def power(self):
        pass

    def coast(self):
        pass


class CarObject(Car):

    def engine(self):
        print("Engine - 4G63")

    def power(self):
        print("Power is 250Hp")

    def coast(self):
        print("Coast is 15k$")

car = CarObject()
car.template_method()
