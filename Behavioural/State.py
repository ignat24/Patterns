from abc import ABC, abstractmethod


class StateLight(ABC):

    @abstractmethod
    def get_color(self):
        pass


class RedLight(StateLight):

    def get_color(self):
        return "Red light"


class YellowLight(StateLight):

    def get_color(self):
        return "Yellow light"


class BlueLight(StateLight):

    def get_color(self):
        return "Blue light"


class Lamp:

    def __init__(self):
        self._current_state = None
        self._states = self.get_states()

    def get_states(self):
        return [BlueLight(), RedLight(), YellowLight()]

    def next_state(self):
        if self._current_state is None:
            self._current_state=self._states[0]
        else:
            index = self._states.index(self._current_state)
            if index < len(self._states) - 1:
                index +=1
            else:
                index = 0
            self._current_state = self._states[index]
            print(self._current_state)
        return self._current_state

    def light(self):
        state = self.next_state()
        print(state.get_color())


lamp = Lamp()
for _ in range(3):
    lamp.light()