'''
    Using ABC (Abstract Base Class), we can remove dependency of class,
    And write clean code.
'''
from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):

    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):

    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    '''
        LightBuld and Fan class is not depend on ElectricPowerSwitch class,
        we replace dependency using ABC (Abstract Base Class) 
    '''

    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()

f = Fan()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()