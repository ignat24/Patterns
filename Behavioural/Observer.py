from abc import ABC, abstractmethod


class Object:

    def __init__(self):
        self._data = None
        self._observers = set()

    def follow(self, observer):
        if not isinstance(observer, ObserverBase):
            return "Error!"
        self._observers.add(observer)

    def unfollow(self, observer):
        if not isinstance(observer, ObserverBase):
            return "Error!"
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class ObserverBase(ABC):

    @abstractmethod
    def update(self, data):
        pass


class Observer(ObserverBase):

    def __init__(self, name):
        self._name = name

    def update(self, data):
        print(self._name, "- Update data:", data)


object = Object()
object.follow(Observer("Observer 1"))
object.follow(Observer("Observer 2"))

object.set_data("Root of 9 is 3")




