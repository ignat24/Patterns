from abc import ABC, abstractmethod


# class StateLight(ABC):
#
#     @abstractmethod
#     def get_color(self):
#         pass


class TrafficLightState:
    name = "Light"
    state = []

    def switch(self, action):
        if action.name in self.state:
            print("Current:", self, "switched to",action.name )
            self.__class__ = action
        else:
            print("Error with state:", action.name)

    def __str__(self):
        return self.name


class RedLight(TrafficLightState):

    name = "Red"
    state = ["Yellow", "Green"]


class YellowLight(TrafficLightState):

    name = "Yellow"
    state = ["Red", "Green"]


class GreenLight(TrafficLightState):

    name = "Green"
    state = ["Yellow"]


class TrafficLight:

    def __init__(self):
        self.state = RedLight()

    def change(self, state):
        self.state.switch(state)

    def get_state(self):
        return self.state


tl = TrafficLight()
tl.change(YellowLight)
print(tl.get_state())
print(tl.get_state())

# class TrafficLight:
#     name = "Light"
#     color = []
#
#     def switch(self, action):
#         if action.name in self.color:
#             print("Current:", self, "switched to",action.name )
#             self.__class__ = action
#         else:
#             print("Error with state:", action.name)
#
#     def __str__(self):
#         return self.name
#
# class Lamp:
#
#     def __init__(self, action):
#         self._action = action
#         self._current_state = None
#         self._states = self.get_states()
#
#     def get_states(self):
#         return [GreenLight(), RedLight(), YellowLight()]
#
#     def get_state(self):
#
#
#     def next_state(self):
#         if self._current_state is None:
#             self._current_state=self._states[0]
#         else:
#             index = self._states.index(self._current_state)
#             if index < len(self._states) - 1:
#                 index +=1
#             else:
#                 index = 0
#             self._current_state = self._states[index]
#             print(self._current_state)
#         return self._current_state
#
#     def light(self):
#         return self._current_state
#         # state = self.next_state()
#         # print(state.get_color())
#
#
# lamp = Lamp()
# for _ in range(3):
#     lamp.light()