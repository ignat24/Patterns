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
secondObj.set_instance()
# print("id 1-st object:", id(firstObj))
# print("id 1-st object:", id(secondObj))


class NewSingleton:

    def __new__(cls):
        if not hasattr(cls,"instance"):
            cls.instance = super(NewSingleton, cls).__new__(cls)
        return cls.instance


obj1 = NewSingleton()
print("id 1-st object:", id(obj1))

obj2 = NewSingleton()
print("2-nd object id:", id(obj2))


