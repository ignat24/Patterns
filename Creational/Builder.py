from abc import ABC, abstractmethod

class Builder(ABC):

    def draw_line(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_text(self):
        pass

    def draw_picture(self):
        pass


class Graphic(ABC):

    def draw(self):
        pass


class DrawPicture:

    def __init__(self, line, rectangle, text):
        self.line = line
        self.rectangle = rectangle
        self.text = text

    def draw_picture(self):
        self.line.draw()
        self.rectangle.draw()
        self.text.draw()




class Line(Graphic):

    def draw(self):
        print("- Line")


class Rectangle(Graphic):

    def draw(self):
        print("- Rectangle")


class Text(Graphic):

    def draw(self):
        print("- Text")


class DrawPictureBuilder(Builder):

    def draw_line(self):
        return Line()

    def draw_rectangle(self):
        return Rectangle()

    def draw_text(self):
        return Text()

    def create_picture(self):
        line = self.draw_line()
        rectangle = self.draw_rectangle()
        text = self.draw_text()
        return DrawPicture(line, rectangle, text)


picture = DrawPictureBuilder()
crPicture = picture.create_picture()
crPicture.draw_picture()






# class Graphic:
#
#     def draw(self):
#         pass
#
#     def add(self, obj):
#         pass
#
#     def get_child(self, index):
#         pass
#
#
# class Line(Graphic):
#
#     def draw(self):
#         print("- Line")
#
#
# class Rectangle(Graphic):
#
#     def draw(self):
#         print("- Rectangle")
#
#
# class Text(Graphic):
#
#     def draw(self):
#         print("- Text")
#
#
# class Picture(Graphic):
#
#     def __init__(self):
#         self._children = []
#
#     def draw(self):
#         for obj in self._children:
#             obj.draw()
#
#     def add(self, obj):
#         if isinstance(obj, Graphic) and not obj in self._children:
#             self._children.append(obj)
#
#     def get_child(self, index):
#         return self._children[index]
#
#
#
#
# picture = Picture()
# picture.add(Line())
# picture.add(Rectangle())
# picture.add(Text())
# picture.draw()
#
#
# print("\n")
# line = picture.get_child(0)
# line.draw()
#
