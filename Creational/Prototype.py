from abc import ABC,abstractmethod

class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class MyClass(Prototype):

    def __init__(self, file1, file2):
