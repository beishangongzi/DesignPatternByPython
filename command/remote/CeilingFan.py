class CeilingFan:
    location = ""
    level = 0
    HIGH = 3
    MEDIUM = 2
    LOW = 1

    def __init__(self, location: str):
        self.location = location

    def high(self):
        self.level = self.HIGH
        print(self.location + " ceiling fan is isOn high")

    def medium(self):
        self.level = self.MEDIUM
        print(self.location + " ceiling fan is isOn medium")

    def low(self):
        self.level = self.LOW
        print(self.location + " ceiling fan is isOn low")

    def off(self):
        self.level = 0
        print(self.location + " ceiling fan is off")

    def getSpeed(self):
        return self.level
