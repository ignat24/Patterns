from abc import ABC, abstractmethod


class Feet(ABC):

    @abstractmethod
    def pour_eat(self, pet):
        pass


class StatePet(ABC):

    @abstractmethod
    def state_pet(self):
        pass


class ObserverBase(ABC):

    @abstractmethod
    def update(self, data):
        pass


class Object:

    def __init__(self):
        self._data = None
        self._observers = set()

    def follow(self, observer):
        if not isinstance(observer, ObserverBase):
            return "Error!"
        self._observers.add(observer)

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)


class Observer(ObserverBase):

    def __init__(self, name):
        self._name = name

    def update(self, data):
        print(self._name, "- Update data:", data)


class FedPet(StatePet):

    def state_pet(self):
        return "Pet is fed!"


class HungryPet(StatePet):

    def state_pet(self):
        return "Pet is hungry!"


class Cat:

    def __init__(self):
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
        return self._current_state.state_pet()


class Dog:

    def __init__(self):
        self._states = self.get_states()
        self._current_state = self._states[0]

    def get_states(self):
        return [HungryPet(), FedPet()]

    def next_state(self):
        index = self._states.index(self._current_state)
        if index < len(self._states) - 1:
            index +=1
        else:
            index = 0
        self._current_state = self._states[index]

    def state(self):
        return self._current_state.state_pet()


class FeetCat(Feet):

    def pour_eat(self, pet):
        print("\nPour Whiskas into a cat's bowl!\n ")
        pet.next_state()


class FeetDog(Feet):

    def pour_eat(self, pet):
        print("\nPour Royal Canin into a dog's bowl!\n")
        pet.next_state()


class Strategy:

    def feet(self, pet):
        if isinstance(pet, Cat):
            feetPet = FeetCat()
        elif isinstance(pet, Dog):
            feetPet = FeetDog()
        else:
            print("This is not your pet!")
            return False

        feetPet.pour_eat(pet)





class Iterator:

    def __init__(self, _elements):
        self._elements = _elements
        self._current = 0
        self._pet = Strategy()

    def next(self):
        self._current += 1
        if not self.check_elem(self._current):
            self._current = 0
        self._pet.feet(self._elements[self._current])

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





object = Object()
dogJack = Dog()
catTom = Cat()
object.follow(Observer("First person"))
object.follow(Observer("Second person"))
iterator = Iterator([catTom, dogJack])

print("\nDog")
object.set_data(dogJack.state())
iterator.next()
object.set_data(dogJack.state())

print("\nCat")
object.set_data(catTom.state())
iterator.next()
object.set_data(catTom.state())
# iterator.next()
# catTom.state()
# # dogJack.state()