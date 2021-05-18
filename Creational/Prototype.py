from abc import ABC,abstractmethod
from copy import copy


class Prototype:

    _type = None
    _number = None

    def get_type(self):
        return self._type

    def get_number(self):
        return self._number

    def clone(self):
        pass


class MyClass(Prototype):

    def __init__(self, number):
        self._type = "MyClass"
        self._number = number

    def clone(self):
        return copy(self)


class NewClass(Prototype):

    def __init__(self, number):
        self._type = "NewClass"
        self._number = number

    def clone(self):
        return copy(self)





class Factory:

    def __init__(self):
        self.Myclass5 = MyClass(5)
        self.Myclass10 = MyClass(10)
        self.NewClass20 = NewClass(20)
        self.NewClass30 = NewClass(30)

    def get_myclass_5(self):
        return self.Myclass5.clone()

    def get_myclass_10(self):
        return self.Myclass10.clone()

    def get_newclass_20(self):
        return self.NewClass20.clone()

    def get_newclass_30(self):
        return self.NewClass30.clone()


factory =Factory()




print("Myclass")
instance1 = factory.get_myclass_5()
print(instance1.get_type(), instance1.get_number())

instance2 = factory.get_myclass_10()
print(instance2.get_type(), instance2.get_number())

print(instance1.get_type(), instance1.get_number())

print("\nNew class")
instance3 = factory.get_newclass_20()
print(instance3.get_type(), instance3.get_number())

instance4 = factory.get_newclass_30()
print(instance4.get_type(), instance4.get_number())

print(instance3.get_type(), instance3.get_number())