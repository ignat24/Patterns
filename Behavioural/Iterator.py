from abc import ABC, abstractmethod


class IteratorBase(ABC):

    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def last(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def previous(self):
        pass

    @abstractmethod
    def check_elem(self, index):
        pass

    @abstractmethod
    def get_elem(self, index):
        pass

    @abstractmethod
    def current_elem(self):
        pass


class Iterator(IteratorBase):

    def __init__(self, _elements):
        self._elements = _elements
        self._current = 0

    def first(self):
        return self._elements[0]

    def last(self):
        return self._elements[-1]

    def next(self):
        self._current += 1
        if not self.check_elem(self._current):
            self._current = 0
        return self.current_elem()

    def current_elem(self):
        return self._elements[self._current]

    def previous(self):
        self._current -= 1
        if not self.check_elem(self._current):
            self._current = len(self.current_elem()) - 1
        return self.current_elem()

    def check_elem(self, index):
        lenIterator = len(self._elements) - 1
        return True if index <= lenIterator else False

    def get_elem(self, index):
        if not self.check_elem(index):
            raise IndexError("Not element with this index")
        return self._elements[index]


partOfElements = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth"]

iterator = Iterator(range(5))
print(iterator.current_elem())
iterator.next()
iterator.next()
print(iterator.current_elem())

# print(str.upper("\nNext element:"))
# for _ in range(len(partOfElements)):
#     print(iterator.next())
#
# print(str.upper("\nPrevious element:"))
# for _ in range(len(partOfElements)):
#     print(iterator.previous())
#
# print(str.upper("\ncheck element '4':"))
# print(iterator.check_elem(3))
#
# print(str.upper("\nget element '4':"))
# print(iterator.get_elem(3))
