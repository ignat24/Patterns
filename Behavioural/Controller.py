from abc import ABC, abstractmethod


class WindowBase(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass


class MainWindow(WindowBase):

    def show(self):
        print( "Show main window")

    def hide(self):
        print( "Hide main window")


class HelpWindow(WindowBase):

    def show(self):
        print( "Show help window")

    def hide(self):
        print( "Hide help window")


class TextWindow(WindowBase):

    def show(self):
        print( "Show text window")

    def hide(self):
        print( "Hide text window")


class WindowMediator:

    def __init__(self):
        self.windows = dict.fromkeys(['main', 'help', 'text'])

    def show(self, win):
        for window in self.windows.values():
            if not window is win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_help(self, win):
        self.windows['help'] = win

    def set_text(self, win):
        self.windows['text'] = win


main_window = MainWindow()
help_window = HelpWindow()
text_window = TextWindow()

mediator = WindowMediator()
mediator.set_main(main_window)
mediator.set_text(text_window)
mediator.set_help(help_window)

print("Help window")
mediator.show(help_window)

print("\nText window")
mediator.show(text_window)
