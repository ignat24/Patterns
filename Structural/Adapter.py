from abc import ABC, abstractmethod

class EuropeanSocketInterface(ABC):

    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def neutral(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def earth(self):
        pass


class USASocketInterface:

    def voltage(self):
        pass

    def neutral(self):
        pass

    def live(self):
        pass



class EuropeanSocket(EuropeanSocketInterface):

    def voltage(self):
        return 220

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


class Fridge:
    __power = None

    def __init__(self, power):
        self.__power=power

    def on(self):
        if self.__power.voltage()>110:
            print("Error!!!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Fridge is working!")
            else: print("Not power!")


eurSocket = EuropeanSocket()
adapter = Adapter(eurSocket)
adapter.neutral()
fridge = Fridge(adapter)
fridge.on()