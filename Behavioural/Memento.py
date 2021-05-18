

class Memento:

    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriter:

    def __init__(self, file):
        self.file = file
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return Memento(self.file, self.text)

    def return_step(self, memento):
        self.file = memento.file
        self.text = memento.text


class FileWriterConcreat:

    def save(self, writer):
        self.obj = writer

    def undo(self, writer):
        writer.return_step(self.obj)


conWriter = FileWriterConcreat()

writer = FileWriter("text.txt")
writer.write("Hello everyone!")
print(writer.text, "\n\n")

conWriter.save(writer)

writer.write("How are you?")
print(writer.text, "\n\n")

conWriter.undo(writer)
print(writer.text, "\n\n")


