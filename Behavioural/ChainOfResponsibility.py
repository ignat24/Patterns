from abc import ABC, abstractmethod


class Error(ABC):

    @abstractmethod
    def error(self, codeError):
        pass


class Error404(Error):

    def error(self, codeError):
        if codeError == 404:
            return "Not Found!"


class Error405(Error):

    def error(self, codeError):
        if codeError == 405:
            return "Method Not Allowed!"


class Error505(Error):

    def error(self, codeError):
        if codeError == 505:
            return "HTTP Version Not Supported!"


class Errors:

    def __init__(self):
        self.handler = []

    def add_code_error(self, obj):
        self.handler.append(obj)

    def errors(self, codeError):
        for obj in self.handler:
            code = obj.error(codeError)
            if code:
                return code

        else:
            print("Undefined code")
        # print(words)


user = Errors()
user.add_code_error(Error404())
user.add_code_error(Error405())
user.add_code_error(Error505())


print("404:", user.errors(404))
print("405:", user.errors(405))
print("505:", user.errors(505))
print("700:", user.errors(700))
