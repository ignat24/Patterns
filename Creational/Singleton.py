class Singleton:

    def __new__(cls):
        if not hasattr(cls,"instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

firstObj = Singleton()
print("id 1-st object:", id(firstObj))

secondObj = Singleton()
print("2-nd object id:", id(secondObj))