from abc import ABC, abstractmethod


class AbstractInterface:

    def functional(self):
        raise NotImplemented()


class Bridge(AbstractInterface):

    def __init__(self):
        self.__implementation = None


class Interface1(Bridge):

    def __init__(self, obj):
        self.__obj = obj

    def functional(self):
        print("Interface 1")
        self.__obj.functionality()


class Interface2(Bridge):

    def __init__(self, obj):
        self.__obj = obj

    def functional(self):
        print("Interface 2")
        self.__obj.functionality()



class ImplementationInterface:

    def functionality(self):
        raise NotImplemented()


class ImplementationLinux(ImplementationInterface):

    def functionality(self):
        print("Linux OS")


class ImplementationWindows(ImplementationInterface):

    def functionality(self):
        print("Windows OS")


linux = ImplementationLinux()
windows = ImplementationWindows()

interface = Interface1(linux)
interface.functional()
print("\n")
interface = Interface1(windows)
interface.functional()
print("\n")
interface = Interface2(linux)
interface.functional()
print("\n")
interface = Interface2(windows)
interface.functional()



