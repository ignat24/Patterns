import abc


class Light:

    def turn_on(self):
        print("Light is on!\n")

    def turn_off(self):
        print("Light is off!\n")


class ActionBase(abc.ABC):

    @abc.abstractmethod
    def action(self):
        pass


class LightActionBase(ActionBase):

    def __init__(self, light):
        self.light = light


class LightOn(LightActionBase):

    def action(self):
        self.light.turn_on()


class LightOff(LightActionBase):

    def action(self):
        self.light.turn_off()


class Switch:

    def __init__(self, on_light, off_light):
        self.on_light = on_light
        self.off_light = off_light

    def on_lamp(self):
        self.on_light.action()

    def off_lamp(self):
        self.off_light.action()


light = Light()
on_light = LightOn(light)
off_light = LightOff(light)

switch = Switch(on_light = on_light, off_light = off_light)

switch.on_lamp()
switch.off_lamp()
