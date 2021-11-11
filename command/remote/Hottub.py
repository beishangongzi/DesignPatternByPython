class Hottub:
    isOn = True
    temperature = 0
    def __init__(self):
        pass

    def onFun(self):
        self.isOn = True

    def off(self):
        self.isOn = False

    def bubblesOn(self):
        if self.isOn:
            print("Hottub is bubbling")

    def jetsOff(self):
        if self.isOn:
            print("Hottub jets are off")

    def setTemperature(self, temperature: int):
        self.temperature = temperature

    def heat(self):
        self.temperature = 105
        print("Hottub is heating to a steaming 105 degress")

    def cool(self):
        self.temperature = 98
        print("Hottub is cooling to 98 degress")



