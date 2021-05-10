class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("Called method init")
        else:
            print("Class object already create", self.set_instance())

    @classmethod
    def set_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


print("Create first object:")
firstObj = Singleton()
firstObj.set_instance()
print("\nCreate second object:")
secondObj = Singleton()


class NewSingleton:

    @classmethod
    def __cl
