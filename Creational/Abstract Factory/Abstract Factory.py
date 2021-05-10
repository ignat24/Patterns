from abc import ABC, abstractmethod


class IAbstractFactory(ABC):

    @abstractmethod
    def create_order(self, order):
        pass


class AbstractFactory(IAbstractFactory):

    def __init__(self):
        self.abstractFactory_dict = {
            1:
        }

    def create_order(self, order):
