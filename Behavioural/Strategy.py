from abc import ABC, abstractmethod


class FileDecoder(ABC):

    @abstractmethod
    def decoder(self, filename):
        pass


class FileTxt(FileDecoder):

    def decoder(self, filename):
        return "Decoder .txt"


class FileJson(FileDecoder):

    def decoder(self, filename):
        return "Decoder .json"


class FileLog(FileDecoder):

    def decoder(self, filename):
        return "Decoder .log"


class File:

    def open(self, filename):
        spl = filename.rsplit('.',1)[-1]
        if spl == "txt":
            decoder = FileTxt()
        elif spl == "json":
            decoder = FileJson()
        elif spl == "log":
            decoder = FileLog()
        else:
            return "Impossible to decode!"
        filerange = decoder.decoder(filename)
        return filename, filerange


file = File()
print(file.open("file.txt"))

print(file.open("file.json"))

print(file.open("file.log"))

print(file.open("file.text"))





