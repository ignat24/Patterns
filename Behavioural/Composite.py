from abc import ABC, abstractmethod


class Graphic:

    def draw(self):
        pass

    def add(self, obj):
        pass

    def get_child(self, index):
        pass


class Line(Graphic):

    def draw(self):
        print("- Line")


class Rectangle(Graphic):

    def draw(self):
        print("- Rectangle")


class Text(Graphic):

    def draw(self):
        print("- Text")


class Picture(Graphic):

    def __init__(self):
        self._children = []

    def draw(self):
        for obj in self._children:
            obj.draw()

    def add(self, obj):
        if isinstance(obj, Graphic) and not obj in self._children:
            self._children.append(obj)

    def get_child(self, index):
        return self._children[index]




picture = Picture()
picture.add(Line())
picture.add(Rectangle())
picture.add(Text())
picture.draw()


print("\n")
line = picture.get_child(0)
line.draw()
