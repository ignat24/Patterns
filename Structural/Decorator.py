from abc import ABC, abstractmethod


class AbstractCar(ABC):

    @abstractmethod
    def get_coast(self):
        pass

    @abstractmethod
    def get_power(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass


class Car(AbstractCar):

    def get_coast(self):
        return 25000

    def get_power(self):
        return 200

    def get_weight(self):
        return 1000


class AbstractCarDecorator(AbstractCar):

    def __init__(self, improve):
        self.improve = improve

    def get_coast(self):
        return self.improve.get_coast()

    def get_power(self):
        return self.improve.get_power()

    def get_weight(self):
        return self.improve.get_weight()


class ImprovePower(AbstractCarDecorator):

    def get_power(self):
        return self.improve.get_power() + 50


class IncreaseCoast(AbstractCarDecorator):

    def get_coast(self):
        return self.improve.get_coast() + 1000


car = Car()
print("I have a car with characteristics:")
print("Power =", car.get_power())
print("Coast =", car.get_coast())
print("Weight =", car.get_weight(), "\n")


print("I wont to improve my power by 50:")
improvePower = ImprovePower(car)
print("Power after improving =",  improvePower.get_power(), "\n")

improveCoast = IncreaseCoast(improvePower)
print("But: ")
print("Coast after improving - ", improveCoast.get_coast(),"\n")



print("New characteristics:")
print("Power =", improveCoast.get_power())
print("Coast =", improveCoast.get_coast())
print("Weight =", improveCoast.get_weight(), "\n")






