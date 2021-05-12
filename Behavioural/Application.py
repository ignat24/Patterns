import abc
from time import time


class Strategy:

    def check_strategy(self, pet):
        if isinstance(pet, Dog):
            return FeetDog()
        if isinstance(pet, Cat):
            return FeetCat()
        else:
            return FeetError()


class Observer:

    def __init__(self, name):
        self._name = name

    def update(self, data):
        print(self._name, "- Update data:", data)


class FeetCat:

    def feet(self):
        print("\nPour Whiskas into a cat's bowl!\n ")


class FeetDog:

    def feet(self):
        print("\nPour Royal Canin into a dog's bowl!\n")

class FeetError:

    def feet(self):
        print("I don't know how to feed this pet")



class StatePet(abc.ABC):

    def state_pet(self):
        pass

class FedPet(StatePet):

    def state_pet(self):
        return "is fed!"


class HungryPet(StatePet):

    def state_pet(self):
        return "is hungry!"


class Dog:

    def __init__(self, name):
        self._name = name
        self._states = self.get_states()
        self._current_state = self._states[0]

    def get_states(self):
        return [HungryPet(), FedPet()]

    def next_state(self):
        index = self._states.index(self._current_state)
        if index < len(self._states) - 1:
            index += 1
        else:
            index = 0
        self._current_state = self._states[index]

    def state(self):
        if self._current_state is FedPet():
            return self._current_state.state_pet()
        else:
            return self._current_state.state_pet()


class Cat:

    def __init__(self, name):
        self._name = name
        self._states = self.get_states()
        self._current_state = self._states[1]

    def get_states(self):
        return [HungryPet(), FedPet()]

    def next_state(self):
        index = self._states.index(self._current_state)
        if index < len(self._states) - 1:
            index += 1
        else:
            index = 0
        self._current_state = self._states[index]

    def state(self):
        if self._current_state is FedPet():
            return self._current_state.state_pet()
        else:
            return self._current_state.state_pet()



class Iterator:

    def __init__(self, _elements):
        self._elements = _elements
        self._current = 0

    def next(self):
        self._current += 1
        if not self.check_elem(self._current):
            self._current = 0
            return False

    def current_elem(self):
        return self._elements[self._current]

    def check_elem(self, index):
        lenIterator = len(self._elements) - 1
        return True if index <= lenIterator else False



class Robot:

    def __init__(self, pets):
        self._observers = set()
        self.iterator = Iterator(pets)
        self.strategy = Strategy()

    def show_pets(self):
        i = 1
        while True:
            print(i, self.iterator.current_elem()._name)
            if self.iterator.next() is False:
                break
            i+=1

    def check_state(self):
        while True:
            print(self.iterator.current_elem()._name, self.iterator.current_elem().state())
            if "hungry" in self.iterator.current_elem().state():
                print("Need to feet", self.iterator.current_elem()._name)
                self.strategy.check_strategy(self.iterator.current_elem()).feet()
                self.iterator.current_elem().next_state()
                self.set_data("Robot feet " + str(self.iterator.current_elem()._name))
            # else:
            #     print(self.iterator.current_elem()._name, self.iterator.current_elem().state())
            if self.iterator.next() is False:
                break

    def follow(self, observer):
        if not isinstance(observer, Observer):
            print("Error!")
        self._observers.add(observer)

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

    def main(self):
        t_end = time() + 20
        while time() < t_end:
            if time() % 2 == 0:
                self.check_state()
            if time() % 5 == 0:
                while True:
                    self.iterator.current_elem().next_state()
                    if self.iterator.next() is False:
                        break







dogTom = Dog("Tom")
catBarsik = Cat("Barsik")
pets = [dogTom, catBarsik]
robot = Robot(pets)

robot.follow(Observer("Danil"))
robot.follow(Observer("Timosha"))
robot.main()






